import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Joe", "cat", "meow")

    def test_animal_attributes(self):
        self.assertEqual(self.mammal.name, "Joe")
        self.assertEqual(self.mammal.type, "cat")
        self.assertEqual(self.mammal.sound, "meow")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), f"{self.mammal.name} makes {self.mammal.sound}")

    def test_get_animal_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_if_kingdom_attribute_is_private(self):
        result = self.mammal._Mammal__kingdom
        self.assertEqual(result, "animals")

    def test_get_info(self):
        self.assertEqual(self.mammal.info(), f"{self.mammal.name} is of type {self.mammal.type}")


if __name__ == '__main__':
    unittest.main()
