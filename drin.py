# Exercise 11 - Drink Water Reminder

import time

def drink_water_reminder(interval_in_minutes):
    while True:
        time.sleep(interval_in_minutes * 60)  # Convert minutes to seconds
        print("It's time to drink water!")

if __name__ == "__main__":
    reminder_interval = 30  # Set the reminder interval in minutes
    drink_water_reminder(reminder_interval)
