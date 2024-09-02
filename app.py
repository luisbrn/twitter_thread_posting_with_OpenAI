from flask import Flask, render_template, request, jsonify
import tweepy
import openai

app = Flask(__name__)

# Twitter API credentials
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET = 'your_twitter_api_secret'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'

# OpenAI API credentials
OPENAI_API_KEY = 'your_openai_api_key'
openai.api_key = OPENAI_API_KEY

# Set up Twitter API client
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
)
twitter_api = tweepy.API(auth)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_thread():
    user_input = request.json.get('input')
    
    try:
        # Call OpenAI's API to generate content
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ],
            max_tokens=500,
        )
        
        thread_content = response['choices'][0]['message']['content'].strip()
        return jsonify({'thread_content': thread_content})

    except Exception as e:
        print(f"Error communicating with OpenAI API: {e}")
        return jsonify({'error': 'Failed to generate thread content.'}), 500

@app.route('/post', methods=['POST'])
def post_thread():
    thread_content = request.json.get('thread_content')
    thread_parts = thread_content.split('\n\n')  # Split by double newline into individual tweets

    try:
        previous_tweet_id = None
        for part in thread_parts:
            tweet = twitter_api.update_status(status=part, in_reply_to_status_id=previous_tweet_id)
            previous_tweet_id = tweet.id

        return jsonify({'status': 'Thread posted successfully!'})

    except Exception as e:
        print(f"Error posting to Twitter: {e}")
        return jsonify({'error': 'Failed to post the thread.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
