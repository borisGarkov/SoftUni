function compose(array) {
    let obj = {};

    for (let index = 0; index < array.length; index++) {

        if (index % 2 == 0) {
            obj[array[index]] = Number(array[index + 1])
        };
    }

    console.log(obj)
}

compose(['Yoghurt', '48', 'Rise', '138', 'Apple', '52'])