import keyboard
import time
from threading import Thread
import pyautogui

# Configuration
HOTKEY = 'r'

is_running = False
was_pressed = False


def tap_key(key, hold_time):
    keyboard.press(key)
    time.sleep(hold_time)
    keyboard.release(key)


def anchor_macro():
    global is_running

    while is_running: #keys of hobar please change it to your own keys
        try:
            tap_key('á', 0.01) 
            time.sleep(0.005)
            pyautogui.rightClick()

            tap_key('í', 0.01)
            time.sleep(0.005)
            pyautogui.rightClick()

            tap_key('+', 0.01)
            time.sleep(0.005)
            pyautogui.rightClick()

            time.sleep(0.01)  # loop delay

        except Exception as e:
            print(f"Macro error: {e}")
            is_running = False


def toggle_anchor():
    global is_running

    is_running = not is_running

    if is_running:
        print(f"Anchor Macro ON")
        Thread(target=anchor_macro, daemon=True).start()
    else:
        print("✗ Anchor Macro OFF")

print("Anchor Macro Started!")
print(f"Press {HOTKEY.upper()} to toggle")


while True:

    current = keyboard.is_pressed(HOTKEY)

    if current and not was_pressed:
        toggle_anchor()

    was_pressed = current
    time.sleep(0.01)