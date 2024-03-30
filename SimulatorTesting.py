import unittest
import time
import tkinter as tk
from Simulator import Simulator
from Dashboard import Dashboard
from AutomationSystem import AutomationSystem


class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.dashboard = Dashboard(self.root, AutomationSystem())
        self.simulator = Simulator(self.root, AutomationSystem(), self.dashboard)

    def test_simulator_initialization(self):
        self.assertFalse(self.simulator.is_running)  # to ensure is_running is initially False

    def test_setup_dashboard(self):
        self.simulator.setup()
        # assertions here to check if the dashboard setup is successful

    def test_run_simulation_loop(self):
        self.simulator.setup()
        self.simulator.start()
        time.sleep(5)  # Let the simulation run for a while (adjust time as needed)
        self.assertTrue(self.simulator.is_running)
        self.simulator.stop()

    def test_stop_simulation(self):
        self.simulator.setup()
        self.simulator.start()
        self.simulator.stop()
        self.assertFalse(self.simulator.is_running)  # Ensure the simulation loop stops

    def tearDown(self):
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
