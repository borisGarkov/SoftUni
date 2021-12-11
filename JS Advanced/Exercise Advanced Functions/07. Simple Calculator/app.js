function calculator() {
    let selector1;
    let selector2;
    let result;

    function init(input1, input2, inputResult) {
        selector1 = document.querySelector(input1);
        selector2 = document.querySelector(input2);
        result = document.querySelector(inputResult);
    }

    function add() {
        result.value = Number(selector1.value) + Number(selector2.value);
    }

    function subtract() {
        result.value = Number(selector1.value) - Number(selector2.value);
    }

    return {
        init,
        add,
        subtract,
    }
}


const calculate = calculator();
calculate.init('#num1', '#num2', '#result');
