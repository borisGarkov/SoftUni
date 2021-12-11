from project.card.card import Card


# class TrapCard(Card):
#     damage_points = 120
#     health_points = 5
#
#     def __init__(self, name):
#         Card.__init__(self, name, 120, 5)


class TrapCard(Card):
    def __init__(self, name):
        Card.__init__(self, name, 120, 5)

