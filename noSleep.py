import pyautogui
import time

def press_f13_every_minute():
    pyautogui.FAILSAFE = False
    try:
        while True:
            pyautogui.press('f13')  # Press the F16 key
            time.sleep(60)  # Wait for 1 minute
    except KeyboardInterrupt:
        print("Program interrupted by user.")

if __name__ == "__main__":
    press_f13_every_minute()
