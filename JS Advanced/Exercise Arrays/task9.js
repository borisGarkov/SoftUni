function findMagicalMatrix(params) {
    is_magic = true;

    for (const row of params) {
        for (const col of params) {
            prevSum += col;
        };
    };

    return is_magic
}

findMagicalMatrix([[4, 5, 6],
    [6, 5, 4],
    [5, 5, 5]]
   )