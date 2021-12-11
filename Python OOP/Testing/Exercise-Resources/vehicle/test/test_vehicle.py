import unittest

from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 150)

    def test_vehicle_attributes(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        self.assertEqual(self.vehicle.horse_power, 150)

    def test_drive(self):
        self.vehicle.drive(20)
        self.assertEqual(self.vehicle.fuel, 25)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.drive(50)
        self.assertEqual(str(exc.exception), "Not enough fuel")

    def test_refuel(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 35)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(10)
        self.assertEqual(str(exc.exception), "Too much fuel")

    def test_str(self):
        expected = "The vehicle has 150 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(str(self.vehicle), expected)


if __name__ == '__main__':
    unittest.main()
