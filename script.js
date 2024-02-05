document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Collect data from form
    let formData = {
        venue: document.getElementById('venue').value,
        opponent: document.getElementById('opponent').value,
        time: document.getElementById('time').value,
        // Add other fields as necessary
    };
    
    // Send data to backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response and update the UI
        document.getElementById('predictionResult').textContent = `Prediction: ${data.prediction}`;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('predictionResult').textContent = 'Error making prediction';
    });

    console.log('Sending:', JSON.stringify(formData));

    
});
