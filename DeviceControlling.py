import tkinter as tk

from Devices import SmartLight, Thermostat, SecurityCamera, SmartDevice


class ControlFactory:
    def __init__(self):
        self.control_map = {
            SmartLight: SmartLightDeviceControl,
            Thermostat: ThermostatDeviceControl,
            SecurityCamera: SecurityCameraDeviceControl,
        }

    def create_control(self, master, device, update_callback):
        device_type = type(device)
        if device_type in self.control_map:
            return self.control_map[device_type](master, device, update_callback)
        else:
            raise ValueError("Device type not supported by the control factory.")


class DeviceControl:
    def __init__(self, master, device, update_callback):
        self.master = master
        self.device = device
        self.update_callback = update_callback

    def init(self):
        pass  # Initialize GUI components

    def create_controls(self):
        pass

    def toggle_device(self):
        pass

    def update_controls(self):
        pass

    def update_callback(self):
        # Reconfigure the device control based on device state
        self.update(self.device.state)


# import DeviceControl


class SecurityCameraDeviceControl(DeviceControl):
    def __init__(self, master, device, update_callback):
        super().__init__(master, device, update_callback)
        self.status_label = None
        self.motion_status_label = None
        self.record_button = None

    def create_controls(self):
        # Create a button to toggle recording
        self.record_button = tk.Button(self.master, text="Record", command=self.toggle_recording)
        self.record_button.pack()

        # Create a label for motion status
        self.motion_status_label = tk.Label(self.master, text="Motion: Inactive")
        self.motion_status_label.pack()

        # Create a label for displaying the recording status
        self.status_label = tk.Label(self.master, text="Recording: OFF")
        self.status_label.pack()

    def pack_controls(self):
        self.record_button.pack()
        self.motion_status_label.pack()

    def destroy(self):
        # Custom method to destroy or hide the control

        if self.record_button:
            self.record_button.destroy()
        if self.motion_status_label:
            self.motion_status_label.destroy()

    def update_controls(self):
        # Update motion detection label based on camera status
        if self.device.is_motion_detected():
            self.motion_status_label.config(text="Motion: Detected")
        else:
            self.motion_status_label.config(text="Motion: Inactive")

            # Update the status label based on the recording status of the camera
            if self.device.is_recording:
                self.status_label.config(text="Recording: ON")
            else:
                self.status_label.config(text="Recording: OFF")

    def update_motion_detection(self):
        if not self.device.is_motion_detected():
            self.motion_status_label.config(text="Motion: Inactive")
        # Update motion detection label based on camera status
        else:
            self.motion_status_label.config(text="Motion: Detected")

    def toggle_recording(self):
        if self.device.is_recording:
            self.device.stop_recording()
        else:
            self.device.start_recording()
        self.update_controls()






class SmartLightDeviceControl(DeviceControl):
    def __init__(self, master, device, update_callback):
        super().__init__(master, device, update_callback)
        self.status_label = None
        self.brightness_scale = None
        self.toggle_button = None

    def create_controls(self):
        # Button to toggle the light
        self.toggle_button = tk.Button(self.master, text="Toggle Light", command=self.toggle_device)
        self.toggle_button.pack()

        # Scrollbar for brightness control
        self.brightness_scale = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL,
                                         label="Brightness", command=self.set_brightness)
        self.brightness_scale.pack()

        # Create a label for displaying the status
        self.status_label = tk.Label(self.master, text="Status: OFF")
        self.status_label.pack()

    """def set_brightness(self, level):
        # TODO: Implement setting the brightness level of the smart light
        self.device.adjust_brightness(level)
        pass"""

    def set_brightness(self, level):
        self.device.set_brightness(level)  # Update the brightness level of the smart light

    """def update_controls(self):
        # Implement updating Smart Light controls based on device state
        # For instance, if there are visual indicators or controls that change with the device state,
        # update them here based on the current state of the Smart Light.

        # Example: Checking if the Smart Light is ON or OFF
        if self.device.is_on:
            # If the light is ON, update the GUI components accordingly
            print("The Smart Light is currently ON")
            # Update GUI components to reflect the light being ON
            # Example: Change the color of an indicator or label
        else:
            # If the light is OFF, update the GUI components accordingly
            print("The Smart Light is currently OFF")
            # Update GUI components to reflect the light being OFF
            # Example: Change the color of an indicator or label or hide certain controls"""

    def update_controls(self):

        if self.device.get_status():
            self.status_label.config(text="Status: ON")
        else:
            self.status_label.config(text="Status: OFF")

        if self.device.is_on:
            # Example: Update GUI components to reflect the light being ON
            # For instance, change the text of a label or button to indicate ON state
            self.toggle_button.config(text="Light ON", background="yellow")
        else:
            # Example: Update GUI components to reflect the light being OFF
            # Change the appearance or properties of components to indicate OFF state
            self.toggle_button.config(text="Light OFF", background="grey")

    def toggle_device(self):
        self.device.toggle_device()
        self.update_controls()




class ThermostatDeviceControl(DeviceControl):
    def __init__(self, master, device, update_callback):
        super().__init__(master, device, update_callback)
        self.status_label = None
        self.temperature_scale = None
        self.toggle_button = None

    def create_controls(self):
        # Implement creation of GUI components for Thermostat controls
        self.toggle_button = tk.Button(self.master, text="Toggle Thermostat", command=self.toggle_device)
        self.toggle_button.pack()

        self.temperature_scale = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL,
                                               command=self.set_temperature)
        self.temperature_scale.pack()

        # Create a label for displaying the status
        self.status_label = tk.Label(self.master, text="Status: OFF")
        self.status_label.pack()

    def pack_controls(self):
        # Pack or place the GUI components for the Thermostat control
        self.toggle_button.pack()
        self.temperature_scale.pack()

    def set_temperature(self, temperature):
        # This function is connected to the Scale widget and will update the device's temperature
        self.device.set_temperature(int(temperature))
        self.update_temperature_label()  # Update the temperature label after setting the temperature
        self.update_controls()  # Update the controls including the status label

    def update_controls(self):
        # Update the status label based on the device status
        if self.device.get_status():
            self.status_label.config(text=f"Status: ON\nCurrent temperature is {self.device.temperature}")
        else:
            self.status_label.config(text="Status: OFF")

    def update_temperature_label(self):
        # Get the current temperature from the device
        current_temperature = self.device.get_current_temperature()

        # Update the label or any GUI component showing the temperature
        temperature_label_text = f"Current temperature is {current_temperature}"


    def toggle_device(self):
        self.device.toggle_device()
        self.update_controls()



#control_factory = ControlFactory()

#master_widget = tkinter.Widget  # Your main application window or frame
#device_instance = SmartDevice  # An instance of a device like SmartLight, Thermostat, or SecurityCamera

#device_control = DeviceControl(master_widget, device_instance, None)

# Function to update the GUI
#update_callback_function = device_control.update_callback  # Note: No parentheses after update_callback

#control = control_factory.create_control(master_widget, device_instance, update_callback_function)
#control.create_controls()  # Creates the GUI controls

#control.update_controls()  # Updates the GUI controls based on the device state
