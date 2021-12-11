import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("test", "Heavy", 200, 300)

    def test_init_hardware(self):
        self.assertEqual("test", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(200, self.hardware.capacity)
        self.assertEqual(300, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_install_software_successfully(self):
        software = LightSoftware("Windows", 20, 50)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)

    def test_install_software_unsuccessfully(self):
        software = LightSoftware("Windows", 201, 50)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(exc.exception))

    def test_install_software_unsuccessfully_2(self):
        software = LightSoftware("Windows", 50, 1000)
        with self.assertRaises(Exception) as exc:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(exc.exception))

    def test_uninstall_software(self):
        software = LightSoftware("Windows", 20, 50)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertNotIn(software, self.hardware.software_components)

    # def test_get_light_software_components_count(self):
    #     software = LightSoftware("Windows", 20, 50)
    #     software_2 = LightSoftware("Linux", 20, 50)
    #     self.hardware.install(software)
    #     self.hardware.install(software_2)
    #     self.assertEqual(2, self.hardware.get_light_software_components_count())
    #
    # def test_get_express_software_components_count(self):
    #     software = ExpressSoftware("Windows", 20, 50)
    #     software_2 = ExpressSoftware("Linux", 20, 50)
    #     self.hardware.install(software)
    #     self.hardware.install(software_2)
    #     self.assertEqual(2, self.hardware.get_express_software_components_count())

    # def test_can_install(self):
    #     software = ExpressSoftware("Windows", 20, 50)
    #     self.assertTrue(self.hardware.can_install(software))


if __name__ == "__main__":
    unittest.main()
