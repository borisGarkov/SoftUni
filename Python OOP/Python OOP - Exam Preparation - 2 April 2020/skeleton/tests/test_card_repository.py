import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.card_repository = CardRepository()

    def test_init_player_repository(self):
        self.assertEqual(self.card_repository.count, 0)
        self.assertEqual(self.card_repository.cards, [])

    def test_add_player(self):
        self.card_repository.cards.append(MagicCard("Magic"))
        with self.assertRaises(ValueError) as exc:
            self.card_repository.add(MagicCard("Magic"))
        self.assertEqual(str(exc.exception), "Card Magic already exists!")

    def test_remove_player(self):
        self.card_repository.cards.append(MagicCard("Magic"))
        with self.assertRaises(ValueError) as exc:
            self.card_repository.remove("")
        self.assertEqual(str(exc.exception), "Card cannot be an empty string!")
        self.card_repository.remove("Magic")
        self.assertEqual(self.card_repository.cards, [])

    def test_find_player(self):
        card = MagicCard("Gogo")
        card_2 = MagicCard("Sasho")
        self.card_repository.cards.append(card)
        self.card_repository.cards.append(card_2)
        self.assertEqual(self.card_repository.find("Gogo"), card)
