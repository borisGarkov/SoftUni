import unittest

from project.card.trap_card import TrapCard


class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = TrapCard("card")

    def test_init_card(self):
        self.assertEqual(self.card.name, "card")
        self.assertEqual(self.card.damage_points, 120)
        self.assertEqual(self.card.health_points, 5)

    def test_empty_name(self):
        with self.assertRaises(ValueError) as exc:
            self.card.name = ""
        self.assertEqual(str(exc.exception), "Card's name cannot be an empty string.")

    def test_negative_damage_points(self):
        with self.assertRaises(ValueError) as exc:
            self.card.damage_points = -10
        self.assertEqual(str(exc.exception), "Card's damage points cannot be less than zero.")

    def test_negative_health_points(self):
        with self.assertRaises(ValueError) as exc:
            self.card.health_points = -10
        self.assertEqual(str(exc.exception), "Card's HP cannot be less than zero.")