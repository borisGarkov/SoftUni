from task_01.caretaker import Caretaker
from task_01.cheetah import Cheetah
from task_01.keeper import Keeper
from task_01.lion import Lion
from task_01.tiger import Tiger
from task_01.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        filtered_workers = [w for w in self.workers if w.name == worker_name]
        if not filtered_workers:
            return f"There is no {worker_name} in the zoo"

        worker = filtered_workers[0]
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries_sum = 0
        for w in self.workers:
            salaries_sum += w.salary

        if self.__budget < salaries_sum:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salaries_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_needs_total = 0
        for a in self.animals:
            animals_needs_total += a.get_needs()

        if self.__budget < animals_needs_total:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_needs_total
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        amount_of_lions = list(filter(lambda x: isinstance(x, Lion), self.animals))
        amount_of_tigers = list(filter(lambda x: isinstance(x, Tiger), self.animals))
        amount_of_cheetas = list(filter(lambda x: isinstance(x, Cheetah), self.animals))

        result += f"----- {len(amount_of_lions)} Lions:\n"
        result += "\n".join([lion.__repr__() for lion in amount_of_lions])

        result += f"\n----- {len(amount_of_tigers)} Tigers:\n"
        result += "\n".join([tiger.__repr__() for tiger in amount_of_tigers])

        result += f"\n----- {len(amount_of_cheetas)} Cheetahs:\n"
        result += "\n".join([cheetah.__repr__() for cheetah in amount_of_cheetas])

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        amount_of_keepers = list(filter(lambda x: isinstance(x, Keeper), self.workers))
        amount_of_caretakers = list(filter(lambda x: isinstance(x, Caretaker), self.workers))
        amount_of_vets = list(filter(lambda x: isinstance(x, Vet), self.workers))

        result += f"----- {len(amount_of_keepers)} Keepers:\n"
        result += "\n".join([keeper.__repr__() for keeper in amount_of_keepers])

        result += f"\n----- {len(amount_of_caretakers)} Caretakers:\n"
        result += "\n".join([caretaker.__repr__() for caretaker in amount_of_caretakers])

        result += f"\n----- {len(amount_of_vets)} Vets:\n"
        result += "\n".join([vet.__repr__() for vet in amount_of_vets])

        return result
