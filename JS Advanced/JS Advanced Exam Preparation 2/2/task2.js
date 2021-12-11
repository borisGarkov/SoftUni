class SummerCamp {
    constructor(organizer, location) {
        this.organizer = organizer;
        this.location = location;
        this.priceForTheCamp = {
            "child": 150,
            "student": 300,
            "collegian": 500
        };
        this.listOfParticipants = [];
    }

    registerParticipant(name, condition, money) {
        money = Number(money);

        if (this.priceForTheCamp[condition] == undefined) {
            throw new Error('Unsuccessful registration at the camp.');
        }

        let isNamePresent = false;
        this.listOfParticipants.forEach((element) => {
            if (element.name == name) {
                return isNamePresent = true;
            }
        })

        if (isNamePresent) {
            return `The ${name} is already registered at the camp.`
        }

        let priceForStay = Number(this.priceForTheCamp[condition]);

        if (money < priceForStay) {
            return 'The money is not enough to pay the stay at the camp.'
        }

        this.listOfParticipants.push({
            name,
            condition,
            power: 100,
            wins: 0
        })

        return `The ${name} was successfully registered.`
    }

    unregisterParticipant(name) {
        let isNamePresent = false;
        this.listOfParticipants.forEach((element) => {
            if (element.name == name) {
                return isNamePresent = true;
            }
        })

        if (isNamePresent == false) {
            throw new Error(`The ${name} is not registered in the camp.`)
        }

        this.listOfParticipants = this.listOfParticipants.filter(person => person.name != name);
        return `The ${name} removed successfully.`
    }

    timeToPlay(typeOfGame, participant1, participant2) {

        let isParticipant1Present = false;
        let isParticipant2Present = false;


        this.listOfParticipants.forEach((element) => {
            if (element.name == participant1) {
                return isParticipant1Present = true;
            }
        })

        this.listOfParticipants.forEach((element) => {
            if (element.name == participant2) {
                return isParticipant2Present = true;
            }
        })

        if (participant2 == undefined) {
            if (isParticipant1Present == false) {
                throw new Error('Invalid entered name/s.')
            }
        } else if (isParticipant1Present == false || isParticipant2Present == false) {
            throw new Error('Invalid entered name/s.')
        }
        
        let player1 = this.listOfParticipants[this.listOfParticipants.map(x => x.name).indexOf(participant1)];

        if (typeOfGame == 'WaterBalloonFights') {
            let player2 = this.listOfParticipants[this.listOfParticipants.map(x => x.name).indexOf(participant2)];

            if (player1.condition != player2.condition) {
                throw new Error('Choose players with equal condition.')
            }

            if (player1.power > player2.power) {
                player1.wins += 1;
                return `The ${player1.name} is winner in the game ${typeOfGame}.`
            } else if (player1.power < player2.power) {
                player2.wins += 1;
                return `The ${player2.name} is winner in the game ${typeOfGame}.`
            } else {
                return 'There is no winner.'
            }
        }

        if (typeOfGame == 'Battleship') {
            player1.power += 20;
            return `The ${player1.name} successfully completed the game ${typeOfGame}.`
        }

    }

    toString() {
        let result = [];
        result.push(`${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`);
        
        for (const element of this.listOfParticipants.sort((a, b) => (b.wins - a.wins))) {
            result.push(`${element.name} - ${element.condition} - ${element.power} - ${element.wins}`)
        }

        return result.join('\n');
    }
}