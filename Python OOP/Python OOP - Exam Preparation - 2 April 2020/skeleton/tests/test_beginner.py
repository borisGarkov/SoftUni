import unittest

from project.player.beginner import Beginner


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Beginner("Gogo")

    def test_init_player(self):
        self.assertEqual(self.player.username, "Gogo")
        self.assertEqual(self.player.health, 50)

    def test_empty_username(self):
        with self.assertRaises(ValueError) as exc:
            self.player.username = ""
        self.assertEqual(str(exc.exception), "Player's username cannot be an empty string.")

    def test_negative_health(self):
        with self.assertRaises(ValueError) as exc:
            self.player.health = -50
        self.assertEqual(str(exc.exception), "Player's health bonus cannot be less than zero.")
        self.player.health = 0
        self.assertEqual(self.player.is_dead, True)

    def test_player_take_damage(self):
        self.player.take_damage(50)
        self.assertEqual(self.player.health, 0)
        with self.assertRaises(ValueError) as exc:
            self.player.take_damage(-200)
        self.assertEqual(str(exc.exception), "Damage points cannot be less than zero.")