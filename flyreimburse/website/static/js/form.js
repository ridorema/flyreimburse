document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('cardiologyForm');
    const sections = document.querySelectorAll('.form-section');
    const progressBar = document.querySelector('.progress');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const submitBtn = document.getElementById('submitBtn');
    let currentSection = 0;

    function updateButtons() {
        prevBtn.style.display = currentSection === 0 ? 'none' : 'block';
        if (currentSection === sections.length - 1) {
            nextBtn.style.display = 'none';
            submitBtn.style.display = 'block';
        } else {
            nextBtn.style.display = 'block';
            submitBtn.style.display = 'none';
        }
    }

    function updateProgress() {
        const progress = ((currentSection + 1) / sections.length) * 100;
        progressBar.style.width = `${progress}%`;
    }

    function showSection(sectionIndex) {
        sections.forEach((section, index) => {
            section.classList.toggle('active', index === sectionIndex);
        });
        updateButtons();
        updateProgress();

        // If moving to section 2, update the flight information summary
        if (sectionIndex === 1) {
            updateFlightSummary();
        }
    }

    function updateFlightSummary() {
        // Get values from section 1
        const flightNumber = document.getElementById('flightNumber').value; // Typo in ID ('flightNumber')!
        const airline = document.getElementById('airline').value;
        const departureTime = document.getElementById('departureTime').value;
        const arrivalTime = document.getElementById('arrivalTime').value;

        // Create or update the summary div in section 2
        const section2 = document.querySelector('[data-section="2"]');
        let summaryDiv = section2.querySelector('.flight-summary');

        if (!summaryDiv) {
            summaryDiv = document.createElement('div');
            summaryDiv.className = 'flight-summary';
            section2.insertBefore(summaryDiv, section2.firstChild);
        }

        // Update the summary content
        summaryDiv.innerHTML = `
            <div class="summary-box">
                <h3>Flight Details:</h3>
                <p><strong>Flight Number:</strong> ${flightNumber || 'Not provided'}</p>
                <p><strong>Airline:</strong> ${airline || 'Not selected'}</p>
                <p><strong>Departure Time:</strong> ${departureTime || 'Not provided'}</p>
                <p><strong>Arrival Time Time:</strong> ${arrivalTime || 'Not provided'}</p>
            </div>
        `;
    }

    prevBtn.addEventListener('click', () => {
        if (currentSection > 0) {
            currentSection--;
            showSection(currentSection);
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentSection < sections.length - 1) {
            currentSection++;
            showSection(currentSection);
        }
    });

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Form submitted successfully!');
    });

    // Initialize
    updateButtons();
    updateProgress();
});