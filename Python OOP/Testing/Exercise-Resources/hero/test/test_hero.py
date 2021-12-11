import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Gogo", 10, 50, 20)
        self.enemy = Hero("Sasho", 10, 50, 20)

    def test_hero_attributes(self):
        self.assertEqual(self.hero.username, "Gogo")
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 50)
        self.assertEqual(self.hero.damage, 20)

        self.assertEqual(self.enemy.username, "Sasho")
        self.assertEqual(self.enemy.level, 10)
        self.assertEqual(self.enemy.health, 50)
        self.assertEqual(self.enemy.damage, 20)

    def test_if_enemy_name_equals_hero_name(self):
        with self.assertRaises(Exception) as exc:
            self.hero.battle(Hero("Gogo", 20, 50, 20))
        self.assertEqual(str(exc.exception), "You cannot fight yourself")

    def test_if_health_less_than_or_equal_to_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(self.enemy)
        self.assertEqual(str(exc.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_if_health_less_than_zero(self):
        self.hero.health = -5
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(self.enemy)
        self.assertEqual(str(exc.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_if_enemy_health_less_than_or_equal_to_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(self.enemy)
        self.assertEqual(str(exc.exception), "You cannot fight Sasho. He needs to rest")

    def test_if_battle_result_is_draw(self):
        self.enemy.health = 10
        self.assertEqual(self.hero.battle(self.enemy), "Draw")

    def test_if_battle_result_is_win(self):
        self.enemy.health = 1
        self.enemy.damage = 1
        self.assertEqual(self.hero.battle(self.enemy), "You win")
        self.assertEqual(11, self.hero.level)
        self.assertEqual(45, self.hero.health)
        self.assertEqual(25, self.hero.damage)

    def test_if_battle_result_is_loss(self):
        self.hero.damage = 1
        self.enemy.health = 120
        self.assertEqual(self.hero.battle(self.enemy), "You lose")
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(115, self.enemy.health)
        self.assertEqual(25, self.enemy.damage)

    def test_hero_str_method(self):
        hero = Hero("Gogo", 10, 50, 20)
        expected_result = "Hero Gogo: 10 lvl\n" \
                          "Health: 50\n" \
                          "Damage: 20\n"
        self.assertEqual(hero.__str__(), expected_result)


if __name__ == '__main__':
    unittest.main()
