import unittest

from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("name", 100, 2)

    def test_init_room(self):
        self.assertEqual("name", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_negative_expenses(self):
        with self.assertRaises(ValueError) as exc:
            self.room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(exc.exception))


if __name__ == '__main__':
    unittest.main()
