import unittest

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.test = Hardware("test", "heavy", 200, 300)

    def test_initialized(self):
        self.assertEqual("test", self.test.name)
        self.assertEqual("heavy", self.test.type)
        self.assertEqual(200, self.test.capacity)
        self.assertEqual(300, self.test.memory)
        self.assertEqual([], self.test.software_components)

    def test_unsuccessful_install(self):
        software = LightSoftware("light", 200, 300)
        with self.assertRaises(Exception) as exc:
            self.test.install(software)
        self.assertEqual("Software cannot be installed", str(exc.exception))
        self.assertEqual(0, len(self.test.software_components))

    def test_successful_install(self):
        software = LightSoftware("light", 100, 100)
        self.test.install(software)
        self.assertEqual(1, len(self.test.software_components))

    def test_uninstall(self):
        software = LightSoftware("light", 100, 100)
        self.test.install(software)
        self.assertEqual(1, len(self.test.software_components))
        self.test.uninstall(software)
        self.assertEqual(0, len(self.test.software_components))


if __name__ == '__main__':
    unittest.main()
