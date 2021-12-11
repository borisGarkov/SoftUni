class Movie {
    constructor(movieName, ticketPrice) {
        this.movieName = movieName;
        this.ticketPrice = Number(ticketPrice);
        this.screenings = [];
        this.totalProfit = 0;
        this.totalTickets = 0;
    }

    checkIfScreeningIsPresent(date, hall) {
        let result = false; 

        this.screenings.forEach(element => {
            if (element.date == date && element.hall == hall) {
                result = true;
            }
        })
        return result
    }

    newScreening(date, hall, description) {
        if (this.checkIfScreeningIsPresent(date, hall)) {
            throw Error(`Sorry, ${hall} hall is not available on ${date}`)
        }

        this.screenings.push({
            date: date,
            hall: hall,
            description: description,
        })

        return `New screening of ${this.movieName} is added.`
    }

    endScreening(date, hall, soldTickets) {
        if (!this.checkIfScreeningIsPresent(date, hall)) {
            throw new Error(`Sorry, there is no such screening for ${this.movieName} movie.`)
        }

        let runningProfit = soldTickets * this.ticketPrice;
        this.totalProfit += runningProfit;
        this.totalTickets += soldTickets;

        this.screenings = this.screenings.filter(el => (el.hall != hall) || (el.date != date));

        return `${this.movieName} movie screening on ${date} in ${hall} hall has ended. Screening profit: ${runningProfit}`
    }

    toString() {
        let result = `${this.movieName} full information:\n`;
        result += `Total profit: ${(this.totalProfit).toFixed(0)}$\nSold Tickets: ${this.totalTickets}\n`
        
        if (this.screenings.length > 0) {

            result += 'Remaining film screenings:\n';
            result += this.screenings
            .sort((a, b) => a.hall.localeCompare(b.hall))
            .map(el => `${el.hall} - ${el.date} - ${el.description}`)
            .join('\n');

        } else {
            result += 'No more screenings!';
        }

        return result;
    }
}

let m = new Movie('Wonder Woman 1984', '10.00');
console.log(m.newScreening('October 2, 2020', 'IMAX 3D', `3D`));
console.log(m.newScreening('October 3, 2020', 'Main', `regular`));
console.log(m.newScreening('October 4, 2020', 'IMAX 3D', `3D`));
console.log(m.endScreening('October 2, 2020', 'IMAX 3D', 150));
console.log(m.endScreening('October 3, 2020', 'Main', 78));
console.log(m.toString());

m.newScreening('October 4, 2020', '235', `regular`);
m.newScreening('October 5, 2020', 'Main', `regular`);
m.newScreening('October 3, 2020', '235', `regular`);
m.newScreening('October 4, 2020', 'Main', `regular`);
console.log(m.toString());
