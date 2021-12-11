from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    # The FreshwaterFish could only live in FreshwaterAquarium!
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += 3


# fish = FreshwaterFish("test", "test2", 2)
# fish.eat()
# print(fish.size)