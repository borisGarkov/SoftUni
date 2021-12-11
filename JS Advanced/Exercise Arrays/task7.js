function rearrangeArray(arr) {
    let result = []
    arr.sort((a, b) => a - b);

    // console.log(arr)

    while (arr.length > 0) {
        result.push(arr.shift(), arr.pop());
    }
    
    return result;
};

console.log(rearrangeArray([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))