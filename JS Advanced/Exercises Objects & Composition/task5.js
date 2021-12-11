function compose(input) {
    let result = {};

    for (const iterator of input) {
        let [town, product, price] = iterator.split(' | ')
        price = Number(price)

        if (!result[product]) {
            result[product] = {};
        }
        result[product][town] = price

    }
    
    for (const el in result) {
        sorted = Object.entries(result[el]).sort((a, b) => a[1] - b[1])
        console.log(`${el} -> ${sorted[0][1]} (${sorted[0][0]})`)
    }
}

compose(['Sample Town | Sample Product | 1000',
    'Sample Town | Orange | 2',
    'Sample Town | Peach | 1',
    'Sofia | Orange | 3',
    'Sofia | Peach | 2',
    'New York | Sample Product | 1000.1',
    'New York | Burger | 10']

)