from task_06.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, p):
        for element in self.pokemon:
            if element.name == p:
                self.pokemon.remove(element)
                return f"You have released {p}"
        return "Pokemon is not caught"

    def trainer_data(self):
        str_1 = f"Pokemon Trainer {self.name}\n"
        str_2 = f"Pokemon count {len(self.pokemon)}\n"
        str_3 = ""
        for p in self.pokemon:
            str_3 += "- " + p.pokemon_details() + "\n"

        return str_1 + str_2 + str_3


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
