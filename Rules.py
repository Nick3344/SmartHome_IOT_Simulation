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
        # logic to turn on the light if camera detects motion
        camera = system.get_device_by_id(self.camera)
        if camera and camera.is_motion_detected():
            light = system.get_device_by_id("Light001")  # Assuming the light ID is known
            if light:
                light.turn_on()


    def execute_automation_rules(self):
        for rule in self.rules:
            rule.evaluate(self)
