function sortArray(arr) {
    arr.sort((a, b) => {
        if (a.length > b.length) {
            return 1
        } else if (a.length < b.length) {
            return -1
        } else {
            return a.localeCompare(b)
        }
    })

    console.log(arr.join('\n'));
}

sortArray(
    ['test',
        'Deny',
        'omen',
        'Default']

)