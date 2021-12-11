from project.animals.animal import Mammal
from project.food import Food, Meat, Vegetable, Fruit


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Vegetable" and not food.__class__.__name__ == "Fruit":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(food, 0.1)


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(food, 0.40)


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Vegetable" and not food.__class__.__name__ == "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(food, 0.30)


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if not food.__class__.__name__ == "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.gain_weight(food, 1.00)
