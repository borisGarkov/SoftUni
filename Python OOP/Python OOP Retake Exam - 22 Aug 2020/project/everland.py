from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([r.room_cost + r.expenses for r in self.rooms])
        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result = []
        rooms = []
        for r in self.rooms:
            total_expenses = r.room_cost + r.expenses
            if r.budget < total_expenses:
                result.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
            else:
                result.append(f"{r.family_name} paid {total_expenses:.2f}$ and have {r.budget:.2f}$ left.")
                r.budget -= total_expenses
                rooms.append(r)
        self.rooms.clear()
        self.rooms += rooms
        return "\n".join(result)

    def status(self):
        result = []
        result.append(f"Total population: {sum([r.members_count for r in self.rooms])}")
        child_expenses = 0
        for r in self.rooms:
            result.append(f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, "
                          f"Expenses: {r.expenses:.2f}$")
            n = 1
            for ch in r.children:
                result.append(f"--- Child {n} monthly cost: {ch.get_monthly_expense():.2f}$")
                child_expenses += ch.get_monthly_expense()
                n += 1

            result.append(f"--- Appliances monthly cost: {r.expenses - child_expenses:.2f}$")
        return "\n".join(result)
