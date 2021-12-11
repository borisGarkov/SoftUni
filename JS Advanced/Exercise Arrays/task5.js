function reduceArray(array) {
    biggestNumber = Number.MIN_SAFE_INTEGER;
    let result = [];

    array.reduce((accumulated, currentNumber) => {
        if (currentNumber >= biggestNumber) {
            accumulated.push(currentNumber);
            biggestNumber = currentNumber;
        };

        return accumulated
    }, result);

    return result
};


console.log(reduceArray([1, 3, 8,
    4,
    10,
    12,
    3,
    2,
    24]))