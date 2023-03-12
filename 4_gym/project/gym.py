from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipments = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipments:
            self.equipments.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if ExercisePlan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    @staticmethod
    def get_obj_from_id(it_id, iterable):
        for item in iterable:
            if item.id == it_id:
                return item

    def subscription_info(self, subscription_id: int):
        subscription = self.get_obj_from_id(subscription_id, self.subscriptions)
        customer_id = subscription.customer_id
        customer = self.get_obj_from_id(customer_id, self.customers)
        trainer_id = subscription.trainer_id
        trainer = self.get_obj_from_id( trainer_id, self.trainers)
        plan = [pl for pl in self.plans if pl.trainer_id == trainer_id][0]
        equipment_id = plan.equipment_id
        equipment = self.get_obj_from_id( equipment_id, self.equipments)
        representation = [subscription, customer, trainer, equipment, plan]
        result = '\n'.join([repr(x) for x in representation])
        return result
