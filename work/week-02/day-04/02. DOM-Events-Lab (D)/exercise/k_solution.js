/*-------------------------------- Constants --------------------------------*/

/*-------------------------------- Variables --------------------------------*/

let value1
let value2
let total
let operation

/*------------------------ Cached Element References ------------------------*/

let numbers = document.querySelectorAll(".number");

let operationBtns = document.querySelectorAll(".operation");

let totalDisplay = document.querySelector(".display");

let equalsBtn = document.querySelector(".equals");

let clearBtn = document.querySelector(".clear");

/*-------------------------------- Functions --------------------------------*/


const init = () => {
  totalDisplay.innerText = 0
  total = null
  value1 = null
  value2 = null
  operation = null
}

init()

const renderResult = () => {
  if (operation === "add") {
    total = parseInt(value1) + parseInt(value2)
  } else if (operation === "subtract") {
    total = parseInt(value1) - parseInt(value2)
  } else if (operation === "multiply") {
    total = parseInt(value1) * parseInt(value2)
  } else {
    total = parseInt(value1) / parseInt(value2)
  }
  totalDisplay.innerText = total;
};

const handleOperationBtn = (event) => {
  if (!value1) value1 = 0
  if (value2 != null){
    value1 = renderResult()
    value2 = null
  }
  operation = event.target.id;
  console.log(operation)
};

/*----------------------------- Event Listeners -----------------------------*/

numbers.forEach((number) => {
  number.addEventListener("click", (event) => {
    if (total != null){
      value1 = total
      value2 = null
      total = null
    }
    if (!value1 && !operation) {
      totalDisplay.innerText = event.target.innerText;
      value1 = totalDisplay.innerText;
    } else if (value1 != null && !operation) {
      totalDisplay.innerText += event.target.innerText.toString();
      value1 = totalDisplay.innerText;
    } else if (!value2 && operation) {
      totalDisplay.innerText = event.target.innerText.toString();
      value2 = totalDisplay.innerText;
    } else {
      totalDisplay.innerText += event.target.innerText.toString();
      value2 = totalDisplay.innerText;
    }
  });
});

operationBtns.forEach((operation) => {
  operation.addEventListener("click", handleOperationBtn);
});

equalsBtn.addEventListener("click", (event) => {
  renderResult()  
});

clearBtn.addEventListener("click", (event) => {
  init()
});
