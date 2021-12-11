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
        food_supplies = [s for s in self.supplies if s.__class__.__name__ == "FoodSupply"]
        if not food_supplies:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [s for s in self.supplies if s.__class__.__name__ == "WaterSupply"]
        if not water_supplies:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_supplies = [m for m in self.medicine if m.__class__.__name__ == "Painkiller"]
        if not painkillers_supplies:
            raise IndexError("There are no painkillers left!")
        return painkillers_supplies

    @property
    def salves(self):
        salves_supplies = [m for m in self.medicine if m.__class__.__name__ == "Salve"]
        if not salves_supplies:
            raise IndexError("There are no salves left!")
        return salves_supplies

    def add_survivor(self, survivor: Survivor):
        survivor_name = survivor.name
        names = [s.name for s in self.survivors]
        if survivor_name in names:
            raise ValueError(f"Survivor with name {survivor_name} already exists.")
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
            s.needs -= (2 * s.age)
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")
