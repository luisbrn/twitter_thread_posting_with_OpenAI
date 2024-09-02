document.addEventListener('DOMContentLoaded', function() {
    const generateButton = document.getElementById('generate-button');
    const postButton = document.getElementById('post-button');
    const threadForm = document.getElementById('thread-form');

    // Handle Generate with ChatGPT button click
    if (generateButton) {
        generateButton.addEventListener('click', function() {
            const threadContent = document.getElementById('thread-content').value;

            fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ input: threadContent })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('thread-content').value = data.thread_content;
            })
            .catch(error => console.error('Error:', error));
        });
    }

    // Handle thread preview (form submission)
    if (threadForm) {
        threadForm.addEventListener('submit', function(event) {
            event.preventDefault();  // Prevent the form from submitting the traditional way
            const formData = new FormData(threadForm);
            const threadContent = formData.get('thread_content');

            fetch('/preview', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams(formData)
            })
            .then(response => response.text())
            .then(html => {
                document.open();
                document.write(html);
                document.close();
            })
            .catch(error => console.error('Error:', error));
        });
    }

    // Handle Post to Twitter button click on preview page
    if (postButton) {
        postButton.addEventListener('click', function() {
            const threadContent = document.querySelector('.thread-preview').textContent;

            fetch('/post', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ thread_content: threadContent })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.status);
                window.location.href = '/';
            })
            .catch(error => console.error('Error:', error));
        });
    }
});