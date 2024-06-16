function sendCommand() {
    const command = document.getElementById('commandInput').value;

    fetch('/process-command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ command: command })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Handle the response data, e.g., update the UI or send commands to the robotic hand
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

