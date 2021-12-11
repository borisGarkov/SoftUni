function compose(input) {
    let result = {};

    for (const iterator of input) {
        let [product, price] = iterator.split(' : ');
        let letter = product[0]

        if (!result[letter]) {
            result[letter] = {}
        }

        result[letter][product] = price
    }

    for (const el of Object.keys(result).sort()) {
        console.log(el)
        for (const innerEl of Object.keys(result[el]).sort())
            console.log(`  ${innerEl}: ${result[el][innerEl]}`);
    }
}



compose(
    ['Appricot : 20.4',
        'Fridge : 1500',
        'TV : 1499',
        'Deodorant : 10',
        'Boiler : 300',
        'Apple : 1.25',
        'Anti-Bug Spray : 15',
        'T-Shirt : 10']

)