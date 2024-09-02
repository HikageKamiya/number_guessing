document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('.squareInput');

    inputs.forEach((input, index) => {
        input.addEventListener('input', function () {
            if (input.value.length === 1) {
                // Move to the next input box if there is one
                if (index < inputs.length - 1) {
                    inputs[index + 1].focus();
                }
            }
        });

        input.addEventListener('keydown', function (event) {
            if (event.key === 'Backspace' && input.value.length === 0 && index > 0) {
                // Move to the previous input box if there is one
                inputs[index - 1].focus();
                inputs[index - 1].value = ''; // Optional: clear previous input
            }
        });

        input.addEventListener('keydown', function(event){
            console.log('Key pressed: ', event.key);
            if(event.key === 'Enter' && input.value.length === 1){
                console.log('Flipping input box', input.id);
                input.classList.add('flipped');    // trigger the animation using the class .flip
            }
        });
    });
});
