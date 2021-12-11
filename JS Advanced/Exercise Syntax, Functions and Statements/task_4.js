function getNewDate(year, month, day) {

    let d = new Date(year, month-1, day);
    // let milisecs = 1000 * 60 * 60 * 24;
    d.setDate(d.getDate() - 1); 

    return `${d.getFullYear()}-${d.getMonth()+1}-${d.getDate()}`;
}

console.log(getNewDate(2016, 9, 30))
console.log(getNewDate(2016, 10, 1))