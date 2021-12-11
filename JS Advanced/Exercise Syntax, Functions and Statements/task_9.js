function returnUpperCase(text) {
    text = text.replace(/[\,\!\?\.]/gi, ' ');
    let array = text.split(" ");
    let resultsArray = new Array;
    let i = 0

    for (let index = 0; index < array.length; index++) {
        
        if (array[index] !== '') {
            resultsArray[i] = array[index].toUpperCase()
            i += 1
        }
        
    }
    console.log(resultsArray.join(", "))
}

returnUpperCase('Functions in JS can be nested, i.e. hold other functions')