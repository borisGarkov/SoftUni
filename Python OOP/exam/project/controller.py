from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type != "FreshwaterAquarium" and aquarium_type != "SaltwaterAquarium":
            return "Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        else:
            self.aquariums.append(SaltwaterAquarium(aquarium_name))

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type != "Ornament" and decoration_type != "Plant":
            return "Invalid decoration type."

        if decoration_type == "Ornament":
            self.decorations_repository.decorations.append(Ornament())
        else:
            self.decorations_repository.decorations.append(Plant())

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        filtered_decoration = [d for d in self.decorations_repository.decorations if
                               d.__class__.__name__ == decoration_type]
        filtered_aquarium = [a for a in self.aquariums if a.name == aquarium_name]

        if not filtered_decoration:
            return f"There isn't a decoration of type {decoration_type}."

        if filtered_aquarium and filtered_decoration:
            self.decorations_repository.decorations.remove(filtered_decoration[0])
            filtered_aquarium[0].decorations.append(filtered_decoration[0])
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type != "FreshwaterFish" and fish_type != "SaltwaterFish":
            return f"There isn't a fish of type {fish_type}."

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)

        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        if (aquarium.__class__.__name__ == "FreshwaterAquarium" and fish.__class__.__name__ == "FreshwaterFish") or \
                (aquarium.__class__.__name__ == "SaltwaterAquarium" and fish.__class__.__name__ == "SaltwaterFish"):

            if len(aquarium.fish) + 1 <= aquarium.capacity:
                aquarium.fish.append(fish)
                return f"Successfully added {fish.__class__.__name__} to {aquarium.name}."

            if len(aquarium.fish) + 1 > aquarium.capacity:
                return "Not enough capacity."

            # aquarium.add_fish(fish)
        else:
            return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        prices_fish = sum([f.price for f in aquarium.fish])
        prices_decoration = sum([d.price for d in aquarium.decorations])
        value = prices_fish + prices_decoration
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = []
        for a in self.aquariums:
            result.append(a.__str__())

        return "\n".join(result)

# test = Controller()
# print(test.add_aquarium("SaltwaterAquarium", "test"))
# print(test.add_decoration("Ornament"))
# print(test.add_fish("test", "SaltwaterFish", "gogo", "teest", 12))
# print(test.add_fish("test", "SaltwaterFish", "pesho", "teest", 12))
# print(test.feed_fish("test"))
# print(test.calculate_value("test"))
# print(test.report())
