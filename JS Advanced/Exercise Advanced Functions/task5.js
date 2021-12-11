function add(a) {
    let sum = a

    function add_and_repeat(b) {
        if (b) {
            sum += b
            return add_and_repeat
        }
        else
            return sum;
    }

    add_and_repeat.toString = function () { return sum }

    return add_and_repeat
}

console.log(add(1)(6).toString())