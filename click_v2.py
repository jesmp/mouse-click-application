import pyautogui
from datetime import datetime, timedelta
import time
import random

def get_amount_of_time():
    """"This will get the amount of time the user wants the application to run for in minutes."""
    input_time = input("Enter the amount of time you want the application to run for (in minutes): ")
    end_time = datetime.now() + timedelta(minutes=int(input_time))
    print(f"The application will run until {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    return end_time
    
def start_clicking(end_time):
    """This will start the clicking process."""
    print("Starting the clicking process in 5 seconds...")
    time.sleep(5)

    while datetime.now() < end_time:
        # Variables
        x=random.randint(120,140)
        y=random.randint(500, 900)
        z=random.randint(0, 3)
        random_time=random.randint(3, 120)
        random_scroll=random.randint(-10, 10)

        # Logic
        pyautogui.moveTo(x, y, z)
        print("next click will be in",random_time,"seconds")
        pyautogui.click()
        pyautogui.scroll(random_scroll)
        time.sleep(random_time)
    
    print("Time's up! Stopping the application.")


if __name__ == "__main__":
    end_time = get_amount_of_time()
    start_clicking(end_time)