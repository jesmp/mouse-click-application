import pyautogui
import time
import random

print("Starting in 5 seconds...")
time.sleep(5)

while True:
    # Variables
    x=random.randint(120,140)
    y=random.randint(500, 900)
    z=random.randint(0, 3)
    random_time=random.randint(3, 300)
    random_scroll=random.randint(-10, 10)

    # Logic
    pyautogui.moveTo(x, y, z)
    print("next click will be in",random_time,"seconds")
    pyautogui.click()
    pyautogui.scroll(random_scroll)
    time.sleep(random_time)