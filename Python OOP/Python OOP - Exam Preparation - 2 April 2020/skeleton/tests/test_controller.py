import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_init_controller(self):
        self.assertEqual(len(self.controller.player_repository.players), 0)
        self.assertEqual(len(self.controller.card_repository.cards), 0)

    def test_add_player_to_player_repository(self):
        self.assertEqual("Successfully added player of type Advanced with username: Gogo",
                         self.controller.add_player("Advanced", "Gogo"))
        self.assertEqual("Successfully added player of type Beginner with username: Sasho",
                         self.controller.add_player("Beginner", "Sasho"))

    def test_add_card_to_card_repository(self):
        self.assertEqual("Successfully added card of type MagicCard with name: Magic",
                         self.controller.add_card("Magic", "Magic"))
        self.assertEqual("Successfully added card of type TrapCard with name: Trap",
                         self.controller.add_card("Trap", "Trap"))

    def test_add_card_to_player_repository(self):
        player = Advanced("Sasho")
        card = MagicCard("Magic")
        card_repo = CardRepository()
        card_repo.cards.append(card)
        player_repo = PlayerRepository()
        player_repo.players.append(player)
        self.controller.card_repository = card_repo
        self.controller.player_repository = player_repo
        self.assertEqual("Successfully added card: Magic to user: Sasho",
                         self.controller.add_player_card("Sasho", "Magic"))

    def test_fight(self):
        attacker = Advanced("Sasho")
        enemy = Advanced("Gogo")
        player_repo = PlayerRepository()
        player_repo.players.append(attacker)
        player_repo.players.append(enemy)
        self.controller.player_repository = player_repo
        self.assertEqual("Attack user health 250 - Enemy user health 250",
                         self.controller.fight("Sasho", "Gogo"))

    def test_report_function(self):
        player = Advanced("Sasho")
        card = MagicCard("Magic")
        player.card_repository.cards.append(card)
        card_repo = CardRepository()
        card_repo.cards.append(card)
        player_repo = PlayerRepository()
        player_repo.players.append(player)
        self.controller.card_repository = card_repo
        self.controller.player_repository = player_repo
        expected_result = "Username: Sasho - Health: 250 - Cards 1\n" \
                          "### Card: Magic - Damage: 5\n"
        actual_result = self.controller.report()
        self.assertEqual(expected_result, actual_result)

    def test_report(self):
        attacker = Advanced("Test1")
        enemy = Beginner("Test2")
        c = Controller()
        c.player_repository.add(attacker)
        c.player_repository.add(enemy)
        res = c.report()
        self.assertEqual(res, "Username: Test1 - Health: 250 - Cards 0\nUsername: Test2 - Health: 50 - Cards 0\n")