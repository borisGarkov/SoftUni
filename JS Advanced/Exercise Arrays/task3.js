function addRemoveElements(commands) {

    num = 0;
    results = [];

    for (c of commands) {
        num += 1;

        if (c == 'add') {
            results.push(num); 
        } else {
            results.pop();
        };
    };

    if (results.length == 0) {
        console.log('Empty');
    }

    console.log(results.join('\n'));
};

addRemoveElements(
    ['remove', 
    'remove', 
    'remove']
)