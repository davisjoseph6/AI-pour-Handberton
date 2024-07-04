document.getElementById('send-command').addEventListener('click', function() {
    var command = document.getElementById('command-input').value;
    fetch('/process_command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = `Intent: ${data.intent}\nCommand: ${data.command}`;
    })
    .catch(error => console.error('Error:', error));
});

