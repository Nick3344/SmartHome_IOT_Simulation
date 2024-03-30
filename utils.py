import random
import time

def simulate_motion_detection():
    """Simulates motion detection randomly at intervals."""
    # Simulate motion detection randomly at intervals of 5 to 10 seconds
    time.sleep(random.randint(5, 10))
    return True  # Simulate motion detected after the interval


def random_temperature_change():
    """Simulates random temperature change."""
    return random.uniform(-2.0, 2.0)  # Returns a random float between -2.0 and 2.0
