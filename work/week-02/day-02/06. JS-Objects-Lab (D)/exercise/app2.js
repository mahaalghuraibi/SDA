// استيراد بيانات البوكيمون
const pokemon = require('./data.js');

// الكائن الأساسي
const game = {
  items: [
    { name: "pokeball", quantity: 10 },
    { name: "potion", quantity: 5 },
    { name: "rare candy", quantity: 1 }
  ],
  gyms: [
    { name: "Pewter Gym", difficulty: 2, completed: false },
    { name: "Cerulean Gym", difficulty: 4, completed: false },
    { name: "Vermilion Gym", difficulty: 6, completed: false },
    { name: "Celadon Gym", difficulty: 8, completed: false }
  ],
  party: []
};

// Ex1
console.dir(pokemon, { maxArrayLength: null });
// بعد الفحص نطبع البوكيمون رقم 59
console.log(pokemon.find(p => p.number === 59).name);

// Ex2
console.log(game);

// Ex3
game.difficulty = "Med";

// Ex4
const starterPokemon = pokemon.find(p => p.starter === true);
game.party.push(starterPokemon);

// Ex5
const extra = [];
const pick = (predicate) => {
  const p = pokemon.find(x => predicate(x) && !game.party.some(g => g.number === x.number));
  if (p) extra.push(p);
};
pick(p => p.type === 'fire' && !p.starter);
pick(p => p.type === 'water' && !p.starter);
pick(p => p.hp >= 70 && !p.starter);
game.party.push(...extra);

// Ex6
game.gyms.forEach(g => { if (g.difficulty < 3) g.completed = true; });

// Ex7
const evolveMap = { 1: 2, 4: 5, 7: 8, 25: 26 };
const starterIndex = game.party.findIndex(p => p.starter === true);
if (starterIndex !== -1) {
  const current = game.party[starterIndex];
  const evolved = pokemon.find(p => p.number === evolveMap[current.number]);
  game.party.splice(starterIndex, 1, evolved);
}

// Ex8
game.party.forEach(p => console.log(p.name));

// Ex9
pokemon.filter(p => p.starter).forEach(p => console.log(p.name));

// Ex10
game.catchPokemon = function(pokemonObj) { game.party.push(pokemonObj); };
game.catchPokemon(pokemon.find(p => p.number === 39));

// Ex11
game.catchPokemon = function(pokemonObj) {
  game.party.push(pokemonObj);
  const balls = game.items.find(i => i.name === "pokeball");
  if (balls) balls.quantity -= 1;
};
game.catchPokemon(pokemon.find(p => p.number === 52));

// Ex12
game.gyms.forEach(g => { if (g.difficulty < 6) g.completed = true; });

// Ex13
game.gymStatus = function() {
  const gymTally = { completed: 0, incomplete: 0 };
  game.gyms.forEach(g => g.completed ? gymTally.completed++ : gymTally.incomplete++);
  console.log(gymTally);
};
game.gymStatus();

// Ex14
game.partyCount = function() { return game.party.length; };
console.log(game.partyCount());

// Ex15
game.gyms.forEach(g => { if (g.difficulty < 8) g.completed = true; });

// Ex16
console.log(game);
