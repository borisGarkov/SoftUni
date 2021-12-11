from task_04.customer import Customer
from task_04.equipment import Equipment
from task_04.exercise_plan import ExercisePlan
from task_04.subscription import Subscription
from task_04.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id:int):
        current_sub = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == current_sub.customer_id][0]
        trainer = [t for t in self.trainers if t.id == current_sub.trainer_id][0]
        plan = [p for p in self.plans if p.id == current_sub.exercise_id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]

        return f"{current_sub}\n{customer}\n{trainer}\n{equipment}\n{plan}"
