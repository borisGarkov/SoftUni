class Restaurant {
    constructor(budgetMoney) {
        this.budgetMoney = Number(budgetMoney);
        this.menu = {};
        this.stockProducts = {};
        this.history = [];
        this.mealsCount = Object.keys(this.menu).length;
    }

    loadProducts(products) {

        products.forEach(element => {
            let [productName, quantity, totalPrice] = element.split(' ');
            quantity = Number(quantity);
            totalPrice = Number(totalPrice);

            if (totalPrice > this.budgetMoney) {
                this.history.push(`There was not enough money to load ${quantity} ${productName}`);
                return;
            }

            if (this.stockProducts[productName] == undefined) {
                this.stockProducts[productName] = 0;
            }

            this.stockProducts[productName] += quantity;
            this.budgetMoney -= totalPrice;

            this.history.push(`Successfully loaded ${quantity} ${productName}`)
        });

        return this.history.join('\n')
    }

    addToMenu(meal, productsNeeded, price) {
        price = Number(price);

        if (meal in this.menu) {
            return `The ${meal} is already in the our menu, try something different.`
        }

        this.menu[meal] = {
            products: [],
            price: price,
        };

        productsNeeded.forEach(element => {
            let [productName, productQuantity] = element.split(' ');
            this.menu[meal].products.push({
                productName: productName,
                productQuantity: Number(productQuantity),
            });
        })

        this.mealsCount += 1;

        if (this.mealsCount == 1) {
            return `Great idea! Now with the ${meal} we have 1 meal in the menu, other ideas?`
        } else {
            return `Great idea! Now with the ${meal} we have ${this.mealsCount} meals in the menu, other ideas?`
        }
    }

    showTheMenu() {
        if (this.mealsCount == 0) {
            return 'Our menu is not ready yet, please come later...'
        }

        let result = [];

        Object.entries(this.menu).forEach(element => {
            result.push(`${element[0]} - $ ${element[1].price}`)
        })

        return result.join('\n');
    }

    makeTheOrder(meal) {
        if (this.menu[meal] == undefined) {
            return `There is not ${meal} yet in our menu, do you want to order something else?`
        }

        for (const [product, items] of Object.entries(this.menu)) {
            for (const item of items.products) {
                let productName = item.productName;
                let productQuantity = item.productQuantity;

                if (this.stockProducts[productName] == undefined || this.stockProducts[productName] < productQuantity) {
                    return `For the time being, we cannot complete your order (${meal}), we are very sorry...`
                }
            }
            for (const item of items.products) {
                let productName = item.productName;
                let productQuantity = item.productQuantity;
    
                this.stockProducts[productName] -= productQuantity;
            }
        }

        this.budgetMoney += this.menu[meal].price;
        return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${this.menu[meal].price}.`
    }
}