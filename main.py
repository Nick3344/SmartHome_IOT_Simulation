import tkinter as tk          
from Devices import SmartLight, Thermostat, SecurityCamera
from AutomationSystem import AutomationSystem
from Dashboard import Dashboard
from Simulator import Simulator

def main():
    # Create the root window
    root = tk.Tk()
    root.title("Smart Home Automation")
    root.geometry("400x400+100+100")

    # Create an automation system
    system = AutomationSystem()
    system.discover_devices()  # Discover devices and add them to the system

    # Create a dashboard
    dashboard = Dashboard(root, system)
    dashboard.pack()

    # Create a simulator and start the simulation loop
    simulator = Simulator(root, system, dashboard)
    simulator.start()

    # Run the main loop for the GUI
    root.mainloop()

if __name__ == "__main__":
    main()

