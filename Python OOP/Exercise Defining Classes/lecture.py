class Person:
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}; {self.age}"

    def check(self):
        self.max_age += 1
        return self.max_age


def init(person, name, age):
    person.name = name
    person.age = age


pesho = Person("Pesho", 12)
print(pesho.max_age)
