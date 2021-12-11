import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.player_repo = PlayerRepository()

    def test_init_player_repository(self):
        self.assertEqual(self.player_repo.count, 0)
        self.assertEqual(self.player_repo.players, [])

    def test_add_player(self):
        self.player_repo.players.append(Advanced("Gogo"))
        with self.assertRaises(ValueError) as exc:
            self.player_repo.add(Advanced("Gogo"))
        self.assertEqual(str(exc.exception), "Player Gogo already exists!")

    def test_remove_player(self):
        self.player_repo.players.append(Advanced("Gogo"))
        with self.assertRaises(ValueError) as exc:
            self.player_repo.remove("")
        self.assertEqual(str(exc.exception), "Player cannot be an empty string!")
        self.player_repo.remove("Gogo")
        self.assertEqual(self.player_repo.players, [])

    def test_find_player(self):
        player = Advanced("Gogo")
        player_2 = Advanced("Sasho")
        self.player_repo.players.append(player)
        self.player_repo.players.append(player_2)
        self.assertEqual(self.player_repo.find("Gogo"), player)
