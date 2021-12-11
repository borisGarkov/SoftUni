function getFibonator() {
    let numbers = [0];

    function generate() {
        let firstNumber = numbers[numbers.length - 1];
        let secondNumber = numbers[numbers.length - 2];
        let result = 0;

        if (secondNumber != undefined) {
            result = firstNumber + secondNumber;
        } else {
            result = 1;
        }

        numbers.push(result);
        return result
    }

    return generate
}


let fib = getFibonator();
console.log(fib()); // 1
console.log(fib()); // 1
console.log(fib()); // 2
console.log(fib()); // 3
console.log(fib()); // 5
console.log(fib()); // 8
console.log(fib()); // 13