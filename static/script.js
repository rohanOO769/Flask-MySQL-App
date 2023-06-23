// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    // Fetch the current word from the API
    fetch('/api/test')
        .then(response => response.json())
        .then(data => {
            const wordElement = document.getElementById('word');
            wordElement.textContent = data.word;
        })
        .catch(error => console.error('Error:', error));

    // Handle form submission to change the word
    const form = document.getElementById('wordForm');
    form.addEventListener('submit', event => {
        event.preventDefault();

        const newWord = document.getElementById('newWord').value;

        // Make a POST request to the API to update the word
        fetch('/api/change-word', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ newWord })
        })
        .then(response => response.json())
        .then(data => {
            // Update the current word on the page
            const wordElement = document.getElementById('word');
            wordElement.textContent = data.word;

            // Reset the input field
            document.getElementById('newWord').value = '';
        })
        .catch(error => console.error('Error:', error));
    });
});
