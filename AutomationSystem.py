from Devices import SmartLight, Thermostat, SecurityCamera


# import Devices


# import Rules


class AutomationSystem:
    def __init__(self):
        self.devices = []
        self.rules = []

    def execute_automation_rules(self):
        for rule in self.rules:
            rule.evaluate(self)

    def discover_devices(self):
        # Simulates the discovery of IoT devices on the network
        # For demonstration purposes, let's create and add some sample devices
        light1 = SmartLight("Light001")
        thermostat1 = Thermostat("Thermostat001")
        camera1 = SecurityCamera("Camera001")

        self.add_device(light1)
        self.add_device(thermostat1)
        self.add_device(camera1)

    def add_device(self, device):
        if device not in self.devices:
            self.devices.append(device)

    def remove_device(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                self.devices.remove(device)
                break

    def get_device_by_id(self, device_id):
        for device in self.devices:
            if device.device_id == device_id:
                return device
        return None


class AutomationRule:
    def __init__(self, name):
        self.name = name

    def evaluate(self, automation_system):
        pass


class LightMotionRule(AutomationRule):
    def __init__(self, name, camera):
        super().__init__(name)
        self.camera = camera

    def evaluate(self, system):
        # Define logic to turn on the light if camera detects motion
        camera = system.get_device_by_id(self.camera)
        if camera and camera.is_motion_detected():
            light = system.get_device_by_id("Light001")  # Assuming the light ID is known
            if light:
                light.turn_on()
