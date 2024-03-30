import self
from Devices import SmartLight
from DeviceControlling import ControlFactory
import tkinter as tk


# import AutomationSystem


class Dashboard(tk.Frame):
    def __init__(self, master, system):
        super().__init__(master)
        self.master = master
        self.system = system
        self.currentDeviceControl = None

        self.device_listbox = tk.Listbox(self)
        self.controls_frame = tk.Frame(self)
        self.control_factory = ControlFactory()

        self.create_widgets()
        self.update_device_listbox()

    def create_widgets(self):
        self.device_listbox.pack(side=tk.LEFT)
        self.controls_frame.pack(side=tk.RIGHT)

        self.device_listbox.bind("<<ListboxSelect>>", self.on_device_select)

    def on_device_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            device_id = event.widget.get(index)
            device = self.system.get_device_by_id(device_id)
            self.update_controls_frame(device)

    def update_controls_frame(self, device):
        #if self.currentDeviceControl:
            #self.currentDeviceControl.destroy()  # Remove the current control widget

        self.currentDeviceControl = self.control_factory.create_control(
            self.controls_frame, device, self.update_dashboard
        )

        if self.currentDeviceControl:
            self.currentDeviceControl.create_controls()  # Create controls

            # Pack the control's internal frame or widget, adjust this depending on your structure
            self.currentDeviceControl.pack_controls()

    def update_device_listbox(self):
        self.device_listbox.delete(0, tk.END)
        for device in self.system.devices:
            self.device_listbox.insert(tk.END, device.device_id)

    def update_dashboard(self):
        self.update_device_listbox()
        if self.currentDeviceControl:
           self.currentDeviceControl.update()
           #self.update(self.device.state)

    def update_dashboard(self):
        self.update_device_listbox()
        if self.currentDeviceControl and hasattr(self.currentDeviceControl, 'update') and callable(
                getattr(self.currentDeviceControl, 'update')):
            self.currentDeviceControl.update()






