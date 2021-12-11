function sortTickets(data, sortCriteria) {
    let result = [];

    for (const element of data) {
        let [destination, price, status] = element.split('|');

        result.push(
            {
                destination,
                price: Number(price),
                status,
            }
        )
    }

    // if (sortCriteria == 'price') {
    //     result.sort((a, b) => {
    //         return a[sortCriteria] - b[sortCriteria]
    //     })
    // } else {
    //     result.sort((a, b) => {
    //         return a[sortCriteria].localeCompare(b[sortCriteria])
    //     })
    // }

    result.sort((a, b) => {
        return a[sortCriteria] - b[sortCriteria]
    })

    return result

}

// console.log(sortTickets(['Philadelphia|94.20|available',
//     'New York City|95.99|available',
//     'New York City|95.99|sold',
//     'Boston|126.20|departed'],
//     'destination'
// ))

console.log(sortTickets(['Philadelphia|94.20|available',
    'New York City|95.99|available',
    'Boston|126.20|departed',
    'New York City|95.99|sold'],
    'price'
));