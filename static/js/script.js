// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Job search form validation
    const searchForm = document.querySelector('#job-search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(event) {
            const keyword = document.querySelector('#keyword').value.trim();
            const location = document.querySelector('#location').value.trim();
            const category = document.querySelector('#category').value;
            
            if (!keyword && !location && !category) {
                event.preventDefault();
                alert('Please enter at least one search criteria');
            }
        });
    }

    // Application form validation
    const applicationForm = document.querySelector('#application-form');
    if (applicationForm) {
        applicationForm.addEventListener('submit', function(event) {
            const resume = document.querySelector('#resume').value.trim();
            if (!resume) {
                event.preventDefault();
                alert('Please provide your resume');
            }
        });
    }

    // Job posting form character counter
    const jobDescription = document.querySelector('#description');
    const charCounter = document.querySelector('#char-counter');
    
    if (jobDescription && charCounter) {
        jobDescription.addEventListener('input', function() {
            const remaining = 5000 - this.value.length;
            charCounter.textContent = `${remaining} characters remaining`;
            
            if (remaining < 0) {
                charCounter.classList.add('text-danger');
            } else {
                charCounter.classList.remove('text-danger');
            }
        });
    }

    // Filter toggle for mobile
    const filterToggle = document.querySelector('#filter-toggle');
    const filterSection = document.querySelector('#filter-section');
    
    if (filterToggle && filterSection) {
        filterToggle.addEventListener('click', function() {
            filterSection.classList.toggle('d-none');
        });
    }
});
