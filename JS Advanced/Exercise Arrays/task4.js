function rotateArray(params, countOfRotations) {
    for (let index = 0; index < countOfRotations; index++) {
        params.unshift(params.pop());
    };

    console.log(params.join(' '));
}

rotateArray(
    ['1', 
    '2', 
    '3', 
    '4'], 
    2

)