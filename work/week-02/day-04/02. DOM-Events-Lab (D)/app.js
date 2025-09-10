/*-------------------------------- Constants --------------------------------*/
const calculatorContainer = document.getElementById('calculator');
const displayArea = document.querySelector('.display');


/*-------------------------------- Variables --------------------------------*/





/*------------------------ Cached Element References ------------------------*/





/*----------------------------- Event Listeners -----------------------------*/
calculatorContainer.addEventListener('click', (e) => {
  if (e.target.classList.contains('button')) {
    switch (e.target.textContent) {
      case 'C':
        clearDisplay();
        break;

      case '=':
        evaluate();
        break;

      default:
        addToDisplayArea(e.target.textContent);
    }
  }
});


/*-------------------------------- Functions --------------------------------*/
function clearDisplay() {
  displayArea.textContent = "";
}

function addToDisplayArea(value) {
  displayArea.textContent += value;
}

function deleteOneValue() {
  let currentContent = displayArea.textContent;
  displayArea.textContent = currentContent.slice(0, -1);
}

function evaluate() {
  try {
    let calculation = eval(displayArea.textContent); 
    displayArea.textContent = calculation;
  } catch (error) {
    displayArea.textContent = 'Invalid Operation';
    console.error(error);
  }
}
