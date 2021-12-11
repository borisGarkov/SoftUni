function compose(input) {
    let result = [];

    for (const iterator of input) {
        let [town, latitude, longitude] = iterator.split(' | ');
        town = town.split('| ')[1];
        longitude = Number(longitude.split(' |')[0]);

        if (town != 'Town') {
            let obj = {
                Town: town,
                Latitude: Math.floor(latitude * 100) / 100,
                Longitude: Math.floor(longitude * 100) / 100,
            }

            result.push(obj)
        }
    }

    return JSON.stringify(result)
}

compose(['| Town | Latitude | Longitude |',
    '| Sofia | 42.696552 | 23.32601 |',
    '| Beijing | 39.913818 | 116.363625 |']
)