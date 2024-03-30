import utils  # Importing the utility function for motion detection


# src.devices.smart_device
class SmartDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def toggle_device(self):
        self.status = not self.status

    def get_status(self):
        return self.status


class SecurityCamera(SmartDevice):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.is_recording = False
        self.motion_detected = False

    def is_motion_detected(self):
        return self.motion_detected

    def start_recording(self):
        self.is_recording = True

    def stop_recording(self):
        self.is_recording = False

    def update_motion_detected(self):
        # Simulating motion detection using an external utility function
        self.motion_detected = utils.simulate_motion_detection()  # Update the motion status
        return self.motion_detected



# src.devices.smart_light
"""class SmartLight(SmartDevice):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.brightness = 0

    def set_brightness(self, level):
        if not (0 <= level <= 100):
            raise ValueError("Brightness level must be between 0 and 100")
        self.brightness = level
        # Update the status of the light based on the brightness level
        self.status = self.brightness > 0"""


class SmartLight(SmartDevice):
    def __init__(self, device_id):
        super().__init__(device_id)
        self.brightness = 0

    def set_brightness(self, level):
        try:
            level = int(level)
            if not (0 < level < 100):
                raise ValueError("Brightness level must be between 0 and 100")
            self.brightness = level
            # Update the status of the light based on the brightness level
            self.status = self.brightness > 0
        except ValueError:
            raise ValueError("Brightness level must be a valid integer between 0 and 100")


# src.devices.thermostat
class Thermostat(SmartDevice):
    def __init__(self, device_id, default_temperature=22):
        super().__init__(device_id)
        self.temperature = default_temperature

    def decrease_temperature(self, delta=1):
        self.temperature -= delta

    def increase_temperature(self, delta=1):
        self.temperature += delta

    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_current_temperature(self):
        return self.temperature
