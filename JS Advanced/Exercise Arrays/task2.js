function printNthElement(params, number) {
    let result = []
    
    for (let index = 0; index < params.length; index+=number) {
        result.push(params[index])
    }
    
    return result
}


printNthElement(
    ['5', 
    '20', 
    '31', 
    '4', 
    '20'], 
    2
)