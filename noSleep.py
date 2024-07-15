import pyautogui
import time

def press_f16_every_minute():
    while True:
        pyautogui.press('f16')  # Press the F16 key
        time.sleep(60)  # Wait for 1 minute

# Call the function to start pressing F16 every minute
press_f16_every_minute()
