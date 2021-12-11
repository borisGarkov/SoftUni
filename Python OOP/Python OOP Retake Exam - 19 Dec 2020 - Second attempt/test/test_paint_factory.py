import unittest

from project.bunker import Bunker
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.survivor import Survivor


class TestSurvivor(unittest.TestCase):
    def setUp(self):
        self.player = Survivor("Test", 10)

    def test_init(self):
        self.assertEqual(100, self.player.needs)
        self.assertFalse(self.player.needs_healing)
        self.assertFalse(self.player.needs_sustenance)

    def test_bunker(self):
        bunker = Bunker()
        bunker.add_survivor(self.player)
        medicine = Salve()
        medicine_1 = Painkiller()
        medicine_2 = Painkiller()
        bunker.add_medicine(medicine_1)
        bunker.add_medicine(medicine_2)
        bunker.add_medicine(medicine)
        self.player.health = 80
        # self.assertEqual([medicine], bunker.medicine)
        bunker.heal(self.player, "Painkiller")
        self.assertEqual(100, self.player.health)


if __name__ == '__main__':
    unittest.main()
