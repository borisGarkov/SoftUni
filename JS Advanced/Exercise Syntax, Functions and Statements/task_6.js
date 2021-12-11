function speedCalculator(speed, area) {

    let speedLimits = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20,
    }

    let speedLimit = speedLimits[area]

    if (speed <= speedLimit) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`)
    } else {
        let difference = speed - speedLimit
        let status = ''

        if (difference <= 20) {
            status = 'speeding'
        } else if (difference <= 40) {
            status = 'excessive speeding'
        } else {
            status = 'reckless driving'
        }

        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
    }
}


speedCalculator(40, 'city')
speedCalculator(21, 'residential')
speedCalculator(120, 'interstate')
speedCalculator(200, 'motorway')