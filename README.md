A sleek web-based platform for creating and managing Twitter threads, powered by the ChatGPT API. This application allows users to draft, preview, and post Twitter threads seamlessly from a user-friendly interface.

Features
Generate Twitter Threads: Automatically generate content for your Twitter threads using OpenAI's GPT-4 model.
Preview Threads: Preview your entire Twitter thread before posting.
Post Threads: Post your threads directly to Twitter with a single click.
Technologies Used
Flask: Lightweight web framework for the backend.
Tweepy: Python library for interacting with the Twitter API.
OpenAI API: For generating content using GPT-4.
HTML/CSS/JavaScript: Frontend technologies for a sleek user interface.
Setup and Installation
Prerequisites
Python 3.7 or higher
Twitter Developer account with API keys
OpenAI API key
Installation
Clone the repository:

git clone https://github.com/yourusername/twitter-thread-manager.git
cd twitter-thread-manager
Create a virtual environment (optional but recommended):

python -m venv venv
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate
Install the required Python packages:

pip install -r requirements.txt
Set up your environment variables:

Create a .env file in the root of your project and add the following:
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
OPENAI_API_KEY=your_openai_api_key
Running the Application
Start the Flask application:

python app.py
Access the application:

Open a web browser and go to http://127.0.0.1:5000/ to interact with the application.
Usage
Draft your thread: Enter the content or prompt for your Twitter thread.
Generate content: Click "Generate with ChatGPT" to automatically generate thread content.
Preview your thread: View the entire thread before posting.
Post to Twitter: Once satisfied, post your thread directly to Twitter.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.
