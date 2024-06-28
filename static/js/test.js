document.addEventListener('DOMContentLoaded', (event) => {
    let isConnected = false;
    let port;
    let reader;
    let writer;

    const connectButton = document.getElementById('connect');
    const sendCommandButton = document.getElementById('sendCommand');
    const startCalibrationButton = document.getElementById('startCalibration');
    const commandInput = document.getElementById('commandInput');
    const statusElement = document.getElementById('status');
    const chatInput = document.getElementById('chatInput');
    const sendChatButton = document.getElementById('sendChat');
    const chatResponseElement = document.getElementById('chatResponse');

    connectButton.addEventListener('click'), async () {
        try {
            port = await navigator.serial.requestPort();
            await port.open({ baudRate: 9600 });
    
            writer = port.writable.getWriter();
            reader = port.readable.getReader();
    
            isConnected = true;
            updateStatus('Connected to Arduino');
        } catch (error) {
            
        }
    }