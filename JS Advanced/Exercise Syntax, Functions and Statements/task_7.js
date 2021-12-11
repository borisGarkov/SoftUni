function calcs(number, task1, task2, task3, task4, task5) {

    functions = {
        'chop': function chop(number) { return number /= 2 },
        'dice': function chop(number) { return Math.sqrt(number) },
        'spice': function chop(number) { return number += 1 },
        'bake': function chop(number) { return number *= 3 },
        'fillet': function chop(number) { return number -= (number * 0.2) },
    };

    let tasks = [task1, task2, task3, task4, task5];

    for (let index = 0; index < tasks.length; index++) {
        number = functions[tasks[index]](number)
        console.log(number);
    }
}

functions['chop']

calcs('32', 'chop', 'chop', 'chop', 'chop', 'chop')