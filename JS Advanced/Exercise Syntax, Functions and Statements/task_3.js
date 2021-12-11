function same_numbers(num) {
    let is_digit_same = true;
    let first = num % 10;
    let sum = 0;
    let value = num;

    while (num) {
        if (num % 10 !== first) {
            is_digit_same = false;
            break;
        }

        num = Math.floor(num / 10);
    }

    while (value) {
        sum += value % 10;
        value = Math.floor(value / 10);
    }

    console.log(is_digit_same);
    console.log(sum);
}

same_numbers(2222222)
same_numbers(1234)