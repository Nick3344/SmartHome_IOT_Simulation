import threading
import time
import tkinter as tk


class Simulator(threading.Thread):
    def __init__(self, root, automation_system, dashboard):
        super().__init__()
        self.root = root
        self.automation_system = automation_system
        self.dashboard = dashboard
        self.is_running = False

    def setup(self):
        self.dashboard.pack()
        self.dashboard.update()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.automation_system.execute_automation_rules()
            self.dashboard.update_dashboard()
            time.sleep(3)

    def stop(self):
        self.is_running = False
