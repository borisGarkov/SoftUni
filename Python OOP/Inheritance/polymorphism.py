from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, number):
        self.number = number

    @abstractmethod
    def return_n_n(self):
        pass


class Circle(Shape):
    def __init__(self, number):
        super().__init__(number)

    def return_n_n(self):
        return self.number * self.number


s = Circle(5)
print(s.number)
