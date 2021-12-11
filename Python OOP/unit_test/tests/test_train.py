import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train("test", 50)

    def test_init(self):
        self.assertEqual("test", self.train.name)
        self.assertEqual(50, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add(self):
        self.assertEqual("Added passenger Gogo", self.train.add("Gogo"))

    def test_passenger_exists(self):
        self.train.add("Gogo")
        with self.assertRaises(ValueError) as exc:
            self.train.add("Gogo")
        self.assertEqual("Passenger Gogo Exists", str(exc.exception))

    def test_add_full_capacity(self):
        self.train.capacity = 1
        self.train.add("Gogo")
        with self.assertRaises(ValueError) as exc:
            self.train.add("Gogo")
        self.assertEqual("Train is full", str(exc.exception))

    def test_remove_success(self):
        self.train.add("Gogo")
        self.assertEqual("Removed Gogo", self.train.remove("Gogo"))

    def test_remove_unsuccessfully(self):
        with self.assertRaises(ValueError) as exc:
            self.train.remove("Gogo")
        self.assertEqual("Passenger Not Found", str(exc.exception))


if __name__ == '__main__':
    unittest.main()
