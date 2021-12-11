from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def __str__(self):
        if self.fish:
            string = " ".join([f.name for f in self.fish])
        else:
            string = "none"

        result = [f"{self.name}:", f"Fish: {string}", f"Decorations: {len(self.decorations)}",
                  f"Comfort: {sum([d.comfort for d in self.decorations])}"]

        return "\n".join(result)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish):
        if (fish.__class__.__name__ == "FreshwaterFish" or fish.__class__.__name__ == "SaltwaterFish") and \
                len(self.fish) + 1 <= self.capacity:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

        if len(self.fish) + 1 > self.capacity:
            return "Not enough capacity."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()
