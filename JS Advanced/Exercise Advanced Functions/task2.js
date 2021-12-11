function determineType(...params) {
    let objects = {

    };

    for (const p of params) {
        let type = typeof(p);
        
        console.log(`${type}: ${p}`)

        if (objects[type] == undefined) {
            objects[type] = 0;
        }

        objects[type] += 1;
    }

    for (const obj of Object.entries(objects).sort((a, b) => b[1] - a[1])) {
        console.log(`${obj[0]} = ${obj[1]}`);
    }
}

determineType('cat', 42, function () { console.log('Hello world!'); })