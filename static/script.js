const temperatureInput = document.getElementById('temperature');
const unitSelect = document.getElementById('unit');
const convertBtn = document.getElementById('convertBtn');
const clearBtn = document.getElementById('clearBtn');
const resultsSection = document.getElementById('resultsSection');
const resultsDiv = document.getElementById('results');
const errorMessage = document.getElementById('errorMessage');

// Unit symbols map
const unitSymbols = {
    'Celsius': '°C',
    'Fahrenheit': '°F',
    'Kelvin': 'K'
};

// Event listeners
convertBtn.addEventListener('click', convert);
clearBtn.addEventListener('click', clearFields);
temperatureInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') convert();
});

async function convert() {
    const temperature = temperatureInput.value.trim();
    const unit = unitSelect.value;

    // Validation
    if (!temperature) {
        showError('Please enter a temperature value.');
        return;
    }

    const temp = parseFloat(temperature);
    if (isNaN(temp)) {
        showError('Please enter a valid numeric temperature.');
        return;
    }

    // Hide previous error
    hideError();

    try {
        const response = await fetch('/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                temperature: temp,
                unit: unit
            })
        });

        const data = await response.json();

        if (!response.ok) {
            showError(data.error || 'Conversion failed.');
            return;
        }

        displayResults(data, unit, temp);
    } catch (error) {
        showError('An error occurred. Please try again.');
        console.error('Error:', error);
    }
}

function displayResults(results, fromUnit, temperature) {
    resultsDiv.innerHTML = '';

    // Display original value
    const originalItem = document.createElement('div');
    originalItem.className = 'result-item';
    originalItem.innerHTML = `
        <span class="label">${fromUnit}</span>
        <span class="value">${temperature} ${unitSymbols[fromUnit]}</span>
    `;
    resultsDiv.appendChild(originalItem);

    // Display converted values
    for (const [unit, value] of Object.entries(results)) {
        const item = document.createElement('div');
        item.className = 'result-item';
        item.innerHTML = `
            <span class="label">${unit}</span>
            <span class="value">${value} ${unitSymbols[unit]}</span>
        `;
        resultsDiv.appendChild(item);
    }

    resultsSection.style.display = 'block';
}

function clearFields() {
    temperatureInput.value = '';
    unitSelect.value = 'Celsius';
    resultsSection.style.display = 'none';
    resultsDiv.innerHTML = '';
    hideError();
    temperatureInput.focus();
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

function hideError() {
    errorMessage.style.display = 'none';
}

// Focus on input field when page loads
document.addEventListener('DOMContentLoaded', () => {
    temperatureInput.focus();
});
