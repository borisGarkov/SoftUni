# import unittest
# from project.aquarium.freshwater_aquarium import FreshwaterAquarium
# from project.fish.freshwater_fish import FreshwaterFish
# from project.fish.saltwater_fish import SaltwaterFish
#
#
# class TestDecorations(unittest.TestCase):
#     def setUp(self):
#         self.aquarium = FreshwaterAquarium("test")
#
#     def test_add(self):
#         fish = SaltwaterFish("fish", "test", 5)
#         fish_1 = FreshwaterFish("fish_1", "test", 5)
#         self.assertEqual("", self.aquarium.add_fish(fish))
#
#
#         # expected = "test:\nFish: fish fish_1\nDecorations: 0\nComfort: 0"
#         # self.assertEqual(expected,self.aquarium.__str__())