import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.factory = PaintFactory("Test", 200)

    def test_init(self):
        self.assertEqual("Test", self.factory.name)
        self.assertEqual(200, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)

    def test_property_products(self):
        self.factory.add_ingredient("white", 20)
        self.assertEqual({"white": 20}, self.factory.products)

    def test_add_ingredient_and_ingredient_not_exists(self):
        with self.assertRaises(TypeError) as exc:
            self.factory.add_ingredient("brown", 200)
        self.assertEqual("Ingredient of type brown not allowed in PaintFactory", str(exc.exception))

    def test_add_ingredient_and_capacity_less_than_quantity(self):
        with self.assertRaises(ValueError) as exc:
            self.factory.add_ingredient("white", 201)
        self.assertEqual("Not enough space in factory", str(exc.exception))

    def test_add_ingredient_successfully(self):
        self.factory.add_ingredient("white", 200)
        self.assertEqual({"white": 200}, self.factory.ingredients)

    def test_remove_ingredient(self):
        with self.assertRaises(KeyError) as exc:
            self.factory.remove_ingredient("white", 20)
        self.assertEqual("No such product in the factory", str(exc.exception))

    def test_remove_ingredient_quantity_greater(self):
        self.factory.add_ingredient("white", 20)
        with self.assertRaises(ValueError) as exc:
            self.factory.remove_ingredient("white", 30)
        self.assertEqual("Ingredient quantity cannot be less than zero", str(exc.exception))

    def test_remove_ingredient_successfully(self):
        self.factory.add_ingredient("white", 20)
        self.factory.remove_ingredient("white", 10)
        self.assertEqual({"white": 10}, self.factory.products)

    def test_can_add_method_true(self):
        self.factory.add_ingredient("white", 20)
        self.assertTrue(self.factory.can_add(20))

    def test_repr_method(self):
        self.factory.add_ingredient("white", 20)
        expected = f"Factory name: Test with capacity 200.\n" \
                   f"white: 20\n"
        self.assertEqual(expected, self.factory.__repr__())


if __name__ == '__main__':
    unittest.main()
