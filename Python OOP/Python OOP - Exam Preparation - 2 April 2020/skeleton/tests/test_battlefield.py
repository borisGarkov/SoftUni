import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self) -> None:
        self.attacker = Advanced("Gogo")
        self.enemy = Beginner("Sasho")

    def test_if_player_is_dead(self):
        self.attacker.health = 0
        with self.assertRaises(ValueError) as exc:
            BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(str(exc.exception), "Player is dead!")

    def test_beginner_health_increase(self):
        BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(self.enemy.health, 90)

    def test_advanced_health_increase_with_cards(self):
        self.attacker.card_repository.cards.append(MagicCard("Magic"))
        BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 330)

    def test_attack(self):
        magic_card = MagicCard("Magic")
        magic_card.damage_points = 90
        self.attacker.card_repository.cards.append(magic_card)
        BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(0, self.enemy.health)

    def test_enemy_dies_in_battle(self):
        attacker = Advanced("Test1")
        enemy = Beginner("Test2")
        card = TrapCard("TrapTest")
        card_2 = TrapCard("TrapTest2")
        attacker.card_repository.add(card)
        attacker.card_repository.add(card_2)
        enemy.card_repository.add(card)
        self.assertEqual(attacker.health, 250)
        self.assertEqual(enemy.health, 50)
        enemy.health += 175
        BattleField.fight(attacker, enemy)
        self.assertEqual(attacker.health, 260)
        self.assertEqual(enemy.health, 0)

        self.assertFalse(attacker.is_dead)
        self.assertTrue(enemy.is_dead)