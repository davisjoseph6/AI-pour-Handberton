let isConnected = false;
let port;
let reader;
let writer;

document.getElementById('connect').addEventListener('click', async () => {
    try {
        // Request a serial port and open it with a baud rate of 9600
        port = await navigator.serial.requestPort();
        await port.open({ baudRate: 9600 });

        writer = port.writable.getWriter();
        reader = port.readable.getReader();

        isConnected = true;
        updateStatus('Connected to Arduino');

        // Continuously read data from the serial port
        readSerialData();
    } catch (error) {
        console.error('Connection failed', error);
        updateStatus('Connection failed');
    }
});

document.getElementById('sendChat').addEventListener('click', async () => {
    const message = document.getElementById('chatInput').value;
    fetch('http://localhost:8000/process_chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('chatResponse').textContent = data.response;
        console.log(`Received response: ${JSON.stringify(data)}`);
        // Send the command to the robot if applicable
        if (data.command) {
            sendCommand(data.command);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('chatResponse').textContent = `Error: ${error.message}`;
    });
});

document.getElementById('sendCommand').addEventListener('click', async () => {
    const command = document.getElementById('commandInput').value;
    if (isConnected && writer) {
        await sendCommand(command);
    } else {
        updateStatus('Not connected to Arduino');
    }
});

document.getElementById('startCalibration').addEventListener('click', () => {
    sendCommand('startCalibration');
});

document.querySelectorAll('.up').forEach(button => {
    button.addEventListener('mousedown', () => sendCalibrateCommand(button.parentElement.parentElement.dataset.motor + ':up'));
    button.addEventListener('mouseup', () => sendCalibrateCommand(button.parentElement.parentElement.dataset.motor + ':stop'));
});

document.querySelectorAll('.down').forEach(button => {
    button.addEventListener('mousedown', () => sendCalibrateCommand(button.parentElement.parentElement.dataset.motor + ':down'));
    button.addEventListener('mouseup', () => sendCalibrateCommand(button.parentElement.parentElement.dataset.motor + ':stop'));
});

async function sendCommand(command) {
    try {
        const encoder = new TextEncoder();
        await writer.write(encoder.encode(command + '\n'));
        console.log(`Command sent: ${command}`);
        updateStatus(`Command sent: ${command}`);
    } catch (error) {
        console.error('Failed to send command', error);
        updateStatus('Failed to send command');
    }
}

async function sendCalibrateCommand(command) {
    try {
        if (isConnected && writer) {
            const encoder = new TextEncoder();
            await writer.write(encoder.encode(command + '\n'));
            console.log(`Calibrate command sent: ${command}`);
            updateStatus(`Calibrate command sent: ${command}`);
        } else {
            updateStatus('Not connected to Arduino');
        }
    } catch (error) {
        console.error('Failed to send calibrate command', error);
        updateStatus('Failed to send calibrate command');
    }
}

async function readSerialData() {
    let buffer = '';
    while (isConnected) {
        try {
            const { value, done } = await reader.read();
            if (done) {
                reader.releaseLock();
                break;
            }
            const decoder = new TextDecoder();
            buffer += decoder.decode(value);

            // Process data if a complete line is received
            if (buffer.includes('\n')) {
                const lines = buffer.split('\n');
                buffer = lines.pop(); // Save any incomplete line to buffer

                lines.forEach(line => {
                    console.log(`Received data: ${line}`);
                    processSerialData(line);
                });
            }
        } catch (error) {
            console.error('Failed to read data', error);
            updateStatus('Failed to read data');
            break;
        }
    }
}

function processSerialData(data) {
    const currentTimeRegex = /^CurrentTime(\d+):(\d+)$/;
    const match = currentTimeRegex.exec(data);
    if (match) {
        const fingerIndex = match[1];
        const currentTimeValue = match[2];

        // Check if the element exists before updating
        const currentTimeElement = document.getElementById(`currentTime${fingerIndex}`);
        if (currentTimeElement) {
            currentTimeElement.textContent = `Current Time: ${currentTimeValue}`;
        } else {
            console.warn(`Element with ID currentTime${fingerIndex} not found`);
        }
    }
}

function updateStatus(message) {
    document.getElementById('status').textContent = message;
}

// Add elements to the HTML to display the currentTime values
document.addEventListener('DOMContentLoaded', () => {
    for (let i = 1; i <= 5; i++) {
        const motorControlDiv = document.querySelector(`.motor-control[data-motor="${i}"]`);
        const currentTimeDiv = document.createElement('div');
        currentTimeDiv.id = `currentTime${i}`;
        currentTimeDiv.textContent = 'Current Time: 0';
        motorControlDiv.appendChild(currentTimeDiv);
    }
});
