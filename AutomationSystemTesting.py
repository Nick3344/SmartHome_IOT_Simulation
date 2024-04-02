import unittest  
from AutomationSystem import AutomationSystem
from Devices import SmartLight, Thermostat, SecurityCamera


class TestAutomationSystem(unittest.TestCase):
    def setUp(self):
        self.automation_system = AutomationSystem()

    def test_device_discovery(self):
        # Ensure devices are added successfully during discovery
        self.automation_system.discover_devices()
        self.assertEqual(len(self.automation_system.devices), 3)  # Check if all devices are added

    def test_add_device(self):
        light1 = SmartLight("Light001")
        thermostat1 = Thermostat("Thermostat001")
        camera1 = SecurityCamera("Camera001")

        self.automation_system.add_device(light1)
        self.automation_system.add_device(thermostat1)
        self.automation_system.add_device(camera1)

        self.assertEqual(len(self.automation_system.devices), 3)  # Check if devices are added correctly

    def test_remove_device(self):
        light1 = SmartLight("Light001")
        self.automation_system.add_device(light1)

        self.automation_system.remove_device("Light001")
        self.assertEqual(len(self.automation_system.devices), 0)  # Check if the device is removed

    def test_get_device_by_id(self):
        light1 = SmartLight("Light001")
        self.automation_system.add_device(light1)

        found_device = self.automation_system.get_device_by_id("Light001")
        self.assertEqual(found_device, light1)  # Check if the retrieved device matches the added one

    def tearDown(self):
        pass  # to perform any cleanup if needed


if __name__ == "__main__":
    unittest.main()
