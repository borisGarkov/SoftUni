from collections import deque


def stock_availability(products, action, *args):

    if action == "delivery":
        products = products + list(args)
    elif action == "sell":

        if len(args) == 0:
            products = products[1:]
        elif isinstance(args[0], int):
            products = deque(products)
            index = int(args[0])
            for _ in range(index):
                products.popleft()
        else:
            if len(args) > 0:
                for p in args:
                    if p in products:
                        products = [el for el in products if not el == p]

    return list(products)





print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
