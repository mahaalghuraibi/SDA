/*-------------------------------- Constants --------------------------------*/
const LOOKUP = {
    "1": "red",
    "-1": "blue",
    "0": "white",
    "winner1": 0,
    "winner-1": 0,
}

const WINNING_COMBOS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

/*-------------------------------- Variables --------------------------------*/
let currPlayer;
let board;
let winner;
let xScore = 0
let oScore = 0

/*------------------------ Cached Element References ------------------------*/
const boardEl = document.getElementById("board");


/*----------------------------- Event Listeners -----------------------------*/
boardEl.addEventListener("click", handleClick);


/*-------------------------------- Functions --------------------------------*/
init()
function init() {
    currPlayer = 1;
    winner = null;
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    render();
}

function render() {
    board.forEach((el, idx) => {
        const currEl = document.getElementById(idx);
        // if (!el) currEl.textContent = 0;
        // if (el) currEl.textContent = el;
        currEl.textContent = el ? LOOKUP[el] : "";
        currEl.style.backgroundColor = LOOKUP[el]
    })
}

function handleClick(event) {
    if(board[event.target.id]) return;
    board[event.target.id] = currPlayer;
    currPlayer *= -1;
    winner = checkWinner();
    if (winner) LOOKUP[`winner${winner}`] += 1;
    console.log(winner, "check winner line 48");
    render();
}

function checkWinner() {
    for (const combo of WINNING_COMBOS) {
        if (Math.abs((board[combo[0]] + board[combo[1]] + board[combo[2]])) === 3) return board[combo[0]];
    }
    
    if (board.every(el => el)) return "TIE";

    return null;
}