import keyboard
import time
import pyautogui

HOTKEY = 'x'

is_busy = False
was_pressed = False

def tap_key(key, hold_time):
    keyboard.press(key)
    time.sleep(hold_time)
    keyboard.release(key)

def shield_breaker():
    global is_busy
    if is_busy:
        return

    is_busy = True
    try:
        time.sleep(0.08)

        tap_key('š', 0.01)  #keys of hobar please change it to your own keys
        time.sleep(0.015)
        pyautogui.click()

        time.sleep(0.015)

        tap_key('+', 0.01) #keys of hobar please change it to your own keys
        time.sleep(0.1)
        pyautogui.click()

        print("Cycle done.")
    finally:
        is_busy = False

print("Started. Press X for one cycle. ESC to exit.")

while True:
    currently_pressed = keyboard.is_pressed(HOTKEY)

    if currently_pressed and not was_pressed:
        shield_breaker()

    was_pressed = currently_pressed
    time.sleep(0.01)