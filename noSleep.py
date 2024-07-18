# import pyautogui
from keyboard import press
import time
import os

MAX_LOG_SIZE = 10 * 1024 * 1024  # 10 Megabytes
F13_key=124
def log_message(message, filename='sys.log'):
    bakfile="bak_"+filename
    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        if file_size > MAX_LOG_SIZE:
            if os.path.exists(bakfile):
                os.remove(bakfile)
            os.rename(filename,bakfile)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(filename, 'a') as file:
        file.write(f"{timestamp} - {message}\n")

def press_f13_every_minute():
    # pyautogui.FAILSAFE = False
    try:
        while True:
            press(F13_key)
            # pyautogui.press('f13')  # Press the F16 key
            log_message(f"Pressed F13_key key={F13_key}")
            time.sleep(60)  # Wait for 1 minute
    except KeyboardInterrupt:
        print("Program interrupted by user.")

if __name__ == "__main__":
    press_f13_every_minute()
