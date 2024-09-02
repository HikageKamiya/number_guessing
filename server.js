document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('.squareInput');

    inputs.forEach((input, index) => {
        input.addEventListener('input', function () {
            if (input.value.length === 1) {
                // Move to the next input box if there is one
                if ((index < inputs.length - 1) && (!inputs[index].classList.contains('endOfRow'))) {
                    inputs[index + 1].focus();
                }
            }
        });

        input.addEventListener('keydown', function (event) {
            if (event.key === 'Backspace' && input.value.length === 0 && index > 0) {
                // Move to the previous input box if there is one
                inputs[index - 1].focus();
                inputs[index - 1].value = ''; // Optional: clear previous input
            }else if(event.key === 'Enter'){
                console.log('Flipping input boxes in the row');
                // Get all input boxes in the same row
                const row = input.closest('.numberContainer1, .numberContainer2, .numberContainer3, .numberContainer4, .numberContainer5, .numberContainer6');
                const rowInputs = row.querySelectorAll('.squareInput');
                rowInputs.forEach(box => box.classList.add('correctNum')); // Add class to all inputs in the row
                inputs[index + 1].focus();
                event.preventDefault(); // Prevent form submission if in a form
            }
        });
    });
});

function randomNumGen(){
    let randomNum = Math.floor(Math.random() * (9 - 0 + 1)) + 0;    // generate random number 0~9
    return randomNum;
}

function numberCheck(){
    let idNum = '#input1';
    const helloworld = document.querySelector(idNum);   // get the inputbox's id to change color
    helloworld.classList.add('correctNum'); // color change
}

const firstNum = randomNumGen();
const secondNum = randomNumGen();
const thirdNum = randomNumGen();
const forthNum = randomNumGen();

const numberList = [firstNum, secondNum, thirdNum, forthNum];   // array for .has() check

console.log(`combination = ${firstNum} ${secondNum} ${thirdNum} ${forthNum}`);
console.log(`numberList = ${numberList}`);
console.log(numberCheck());