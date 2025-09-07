const prompt = require('prompt-sync')()

class Gladiator {
    constructor (name, weapon) {
        this.name = name
        this.weapon = weapon
        // Bonus: No invalid weapons allowed. //
        const weaponsAllowed = ['Spear', 'Club', 'Trident']
        if (!weaponsAllowed.includes(this.weapon)) throw new Error('Weapon not allowed. Please select Spear, Club or Trident.')
    }
}

class Arena {
    constructor (name) {
        this.name = name.charAt(0).toUpperCase() + name.slice(1);
        this.gladiators = []
    }
    addGladiator = (gladiator) => {
        if (this.gladiators.length < 2) this.gladiators.push(gladiator)
        else throw new Error('Only two gladiators allowed in the arena at a time.')
    }
    fight = () => {
        let winner
        let loser
        if (this.gladiators.length === 2) {
            let glad1 = this.gladiators[0]
            let glad2 = this.gladiators[1]
            if (glad1.weapon === glad2.weapon) {
                console.log('Warriors are well-matched. No victor declared.')
                // this.gladiators = []
                // Bonus: Use removeGladiator method. //
                this.removeGladiator(glad1.name)
                this.removeGladiator(glad2.name)
            }
            // Bonus: Maximus always wins. //
            if (glad1.name === 'Maximus') {
                winner = glad1
                loser = glad2
            } else if (glad2.name === 'Maximus') {
                winner = glad2
                loser = glad1
            }
            if (glad1.weapon === 'Trident' && glad2.weapon === 'Spear' ||
                glad1.weapon === 'Spear' && glad2.weapon === 'Club' ||
                glad1.weapon === 'Club' && glad2.weapon === 'Trident') {
                    winner = glad1
                    loser = glad2
            } else {
                winner = glad2
                loser = glad1
            }
            console.log(`${winner.name} wins!`)
            // this.removeGladiator(loser.name)
            // Bonus: User is prompted to put thumbs up or down. //
            let thumbsUp = prompt(`Are you satisfied with the outcome? Input 'y' for thumbs up and save the losing warrior; 'n' for thumbs down and send the victor to glory.`)
            if (thumbsUp == 'y') {
                this.removeGladiator(winner.name)
            } else if (thumbsUp == 'n') {
                this.removeGladiator(loser.name)
            }
            return

        } else {
            throw new Error('Not enough gladiators in the arena.')
        }
    }
    // Bonus: Remove gladiator by name. //
    removeGladiator = (gladiatorName) => {
        this.gladiators.forEach((gladiator, i) => {
            if (gladiator.name.toLowerCase() === gladiatorName.toLowerCase()) {
                this.gladiators.splice(i, 1)
                console.log(`${gladiatorName} has been removed from the arena.`)
            }
        })
    }
    // Bonus: The crowd is only entertained if Maximus is in the arena. //
    areYouNotEntertained = (glad1, glad2) => {
        if (glad1.name.toLowerCase() === 'maximus' || 
            glad2.name.toLowerCase() === 'maximus') {
            console.log('The crowd goes wild')
        } else {
            console.log('Where is Maximus? The crowd boos.')
        }
    }
}

// Exercises below. //

// const max = new Gladiator("Maximus", "Trident");
const max = new Gladiator("Maximus", "Club"); // Maximus wins regardless of weapon.
const titus = new Gladiator("Titus", "Spear");
// const andronicus = new Gladiator("Andronicus", "Spear"); // Tie outcome.
const andronicus = new Gladiator("Andronicus", "Club");
const colosseum = new Arena("Colosseum");
console.log(colosseum.name); 
const megalopolis = new Arena("megalopolis");
console.log(megalopolis.name);
colosseum.addGladiator(max);
// colosseum.addGladiator(titus);
colosseum.addGladiator(andronicus);
console.log(colosseum.gladiators.length);
colosseum.fight()