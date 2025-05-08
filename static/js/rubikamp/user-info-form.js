document.addEventListener('DOMContentLoaded', function() {
    const formSteps = document.querySelectorAll('.form-step');
    const stepNumber = {{ step }};
    
    formSteps.forEach(function(step, index) {
        if (index + 1 !== stepNumber) {
            step.style.display = 'none';
        }
    });
});
