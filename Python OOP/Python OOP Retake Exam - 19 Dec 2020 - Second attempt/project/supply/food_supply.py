from project.supply.supply import Supply


class FoodSupply(Supply):
    needs_increase = 20

    def __init__(self):
        super().__init__(20)
