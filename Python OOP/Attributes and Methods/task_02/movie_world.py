from task_02.customer import Customer
from task_02.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += customer.__repr__() + "\n"
        for dvd in self.dvds:
            result += dvd.__repr__() + "\n"
        return result

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        filtered_customers = [customer for customer in self.customers if customer.id == customer_id]
        filtered_dvds = [dvd for dvd in self.dvds if dvd.id == dvd_id]

        if filtered_dvds and filtered_customers:
            dvd_wanted = filtered_dvds[0]
            current_customer = filtered_customers[0]

            if dvd_wanted in current_customer.rented_dvds:
                return f"{current_customer.name} has already rented {dvd_wanted.name}"
            elif dvd_wanted.is_rented:
                return "DVD is already rented"

            if dvd_wanted.age_restriction > current_customer.age:
                return f"{current_customer.name} should be at least {dvd_wanted.age_restriction} to rent this movie"

            current_customer.rented_dvds.append(dvd_wanted)
            dvd_wanted.is_rented = True
            return f"{current_customer.name} has successfully rented {dvd_wanted.name}"

    def return_dvd(self, customer_id, dvd_id):
        filtered_customers = [customer for customer in self.customers if customer.id == customer_id]
        filtered_dvds = [dvd for dvd in self.dvds if dvd.id == dvd_id]

        dvd_wanted = filtered_dvds[0]
        current_customer = filtered_customers[0]

        for dvd in current_customer.rented_dvds:
            if dvd.id == dvd_wanted.id:
                current_customer.rented_dvds.remove(dvd)
                dvd_wanted.is_rented = False
                return f"{current_customer.name} has successfully returned {dvd_wanted.name}"

        return f"{current_customer.name} does not have that DVD"
