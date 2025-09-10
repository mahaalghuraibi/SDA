// Part 1: The Gladiator
class Gladiator {
    constructor(name, weapon) {
        const validWeapons = ["Spear", "Club", "Trident"];
        if (!validWeapons.includes(weapon)) {
            throw new Error(
                `Weapon ${weapon} is not allowed! Choose one of: ${validWeapons.join(", ")}`
            );
        }
        this.name = name;
        this.weapon = weapon;
    }
}

const max = new Gladiator("Maximus", "Trident");
console.log(max.name);
console.log(max.weapon);

//************************************************
// Part 2: The Arena
class Arena {
    constructor(name) {
        this.name = name[0].toUpperCase() + name.slice(1);
        this.gladiators = [];
    }

    addGladiator(gladiator) {
        if (this.gladiators.length < 2) this.gladiators.push(gladiator);
    }

    fight() {
        // must have exactly 2 gladiators
        if (this.gladiators.length !== 2) return;

        const [g1, g2] = this.gladiators;

        // same weapon -> both eliminated
        if (g1.weapon === g2.weapon) {
            this.gladiators = [];
            return;
        }

        // win rules
        const beats = {
            Trident: "Spear",
            Spear: "Club",
            Club: "Trident",
        };

        if (beats[g1.weapon] === g2.weapon) {
            // g1 wins
            this.gladiators = [g1];
        } else {
            // g2 wins
            this.gladiators = [g2];
        }
    }
}
//**********************************************************************
const colosseum = new Arena("colosseum");
console.log(colosseum.name);
console.log(colosseum.gladiators);

const titus = new Gladiator("Titus", "Spear");
colosseum.addGladiator(max);
colosseum.addGladiator(titus);

console.log(colosseum.gladiators.length);
console.log(colosseum.gladiators.map(g => g.name));

colosseum.fight();
console.log(colosseum.gladiators.map(g => g.name)); 
