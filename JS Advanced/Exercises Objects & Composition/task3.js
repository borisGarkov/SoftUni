function compose(obj) {

    function engineSize(engine) {
        if (engine <= 90) {
            return { power: 90, volume: 1800 };
        } else if (engine <= 120) {
            return { power: 120, volume: 2400 };
        } else {
            return { power: 200, volume: 3500 };
        }
    }

    let properWheelSize = obj.wheelsize % 2 == 0 ? obj.wheelsize - 1 : obj.wheelsize

    let result = {
        model: obj.model,
        engine: engineSize(obj.power),
        carriage: {
            type: obj.carriage,
            color: obj.color,
        },
        wheels: new Array(4).fill(properWheelSize, 0, 4),
    };

    return result;
}


console.log(compose(
    {
        model: 'VW Golf II',
        power: 90,
        color: 'blue',
        carriage: 'hatchback',
        wheelsize: 14
    })
)
