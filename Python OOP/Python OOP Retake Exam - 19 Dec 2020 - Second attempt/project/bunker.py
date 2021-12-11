from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        filtered_food = [s for s in self.supplies if s.__class__.__name__ == "FoodSupply"]
        if not filtered_food:
            raise IndexError("There are no food supplies left!")
        return filtered_food

    @property
    def water(self):
        filtered_water = [s for s in self.supplies if s.__class__.__name__ == "WaterSupply"]
        if not filtered_water:
            raise IndexError("There are no water supplies left!")
        return filtered_water

    @property
    def painkillers(self):
        filtered_painkiller = [s for s in self.medicine if s.__class__.__name__ == "Painkiller"]
        if not filtered_painkiller:
            raise IndexError("There are no painkillers left!")
        return filtered_painkiller

    @property
    def salves(self):
        filtered_painkiller = [s for s in self.medicine if s.__class__.__name__ == "Salve"]
        if not filtered_painkiller:
            raise IndexError("There are no salves left!")
        return filtered_painkiller

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        for m in reversed(self.medicine):
            if m.__class__.__name__ == medicine_type and survivor.needs_healing:
                m.apply(survivor)
                self.medicine.remove(m)
                return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        for s in reversed(self.supplies):
            if s.__class__.__name__ == sustenance_type and survivor.needs_sustenance:
                s.apply(survivor)
                self.supplies.remove(s)
                return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")
