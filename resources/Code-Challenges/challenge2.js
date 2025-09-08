const scores = [60, 70, 80, 90]
console.log(scores.length)
console.log(scores[0]);
console.log(scores[3]);
scores.push(25);
console.log(scores);
scores.unshift(3);
console.log(scores);
scores.pop();
console.log(scores);
let removed = scores.shift();   
console.log(removed);           
console.log(scores);   
const doubleScores = scores.map(score => score * 2);
console.log(doubleScores);









