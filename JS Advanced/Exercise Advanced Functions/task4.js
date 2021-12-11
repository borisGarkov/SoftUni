function solution() {

    let supplies = {
        'protein': 0,
        'carbohydrate': 0,
        'fat': 0,
        'flavours': 0,
    };

    let recipes = {
        'apple': function (quantity) {
            for (let index = 0; index < quantity; index++) {
                if (supplies['carbohydrate'] >= 1 && supplies['flavours'] >= 2) {
                    supplies['carbohydrate'] -= 1;
                    supplies['flavours'] -= 2;
                } else {
                    if (supplies['carbohydrate'] < 1) {
                        return `Error: not enough carbohydrate in stock`
                    } else {
                        return `Error: not enough flavours in stock`
                    }
                }
            }

            return 'Success'
        }
    };

    let actions = {
        'restock': function (supply, quantity) { supplies[supply] += quantity; return 'Success' },
        'prepare': function (params) {
            
        },
        'report': function () {
            let result = '';
            for (const key, value of Object.entries) {
                result += `${key}=${supplies[key]} `;
            }
            return result.trim()
        }
    }

    function manage(input) {
        let [action, supply, quantity] = input.split(' ');

        

    }

    return manage
}