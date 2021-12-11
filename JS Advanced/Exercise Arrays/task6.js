function sortArray(params) {
    params.sort((a, b) => a.localeCompare(b))

    for (let index = 0; index < params.length; index++) {
        console.log(`${index + 1}.${params[index]}`)

    }
}

sortArray(["John", "Bob", "Christina", "Ema"])