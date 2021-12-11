function calculate(fruit, money, weight) {

    kilograms = (money / 1000).toFixed(2)
    money *= weight
    money = (money / 1000).toFixed(2)

    console.log(
        `I need $${money} to buy ${kilograms} kilograms ${fruit}.`
        )
}

calculate('orange', 2500, 1.80)
calculate('apple', 1563, 2.35)