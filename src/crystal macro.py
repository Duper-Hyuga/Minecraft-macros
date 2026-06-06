import keyboard
import time
from threading import Thread
import pyautogui

CRYSTAL_HOTKEY = 'x'
OBSIDIAN_HOTKEY = 'y'

is_running = False
crystal_was_pressed = False
obsidian_was_pressed = False


def tap_key(key, hold_time=0.01):
    keyboard.press(key)
    time.sleep(hold_time)
    keyboard.release(key)


def place_one_obsidian():
    try:
        tap_key('ý')
        time.sleep(0.01)

        pyautogui.rightClick()
        time.sleep(0.01)

        tap_key('ž')
        print("Placed one obsidian")

    except Exception as e:
        print(f"Obsidian error: {e}")


def crystal_macro():
    global is_running

    try:
        tap_key('ý') #keys of hobar please change it to your own keys
        time.sleep(0.01)
        pyautogui.rightClick()
        time.sleep(0.01)
        tap_key('ž') #keys of hobar please change it to your own keys

        while is_running:
            pyautogui.rightClick(clicks=5)
            time.sleep(0.003)

            pyautogui.click()
            time.sleep(0.002)

    except Exception as e:
        print(f"Macro error: {e}")
        is_running = False


def toggle_crystal():
    global is_running

    is_running = not is_running

    if is_running:
        print("Crystal Macro ON")
        Thread(target=crystal_macro, daemon=True).start()
    else:
        print("Crystal Macro OFF")


try:
    print("Macro Started!")
    print(f"Press {OBSIDIAN_HOTKEY.upper()} -> place one obsidian")
    print(f"Press {CRYSTAL_HOTKEY.upper()} -> toggle crystal macro")

    while True:

        crystal_pressed = keyboard.is_pressed(CRYSTAL_HOTKEY)
        obsidian_pressed = keyboard.is_pressed(OBSIDIAN_HOTKEY)

        if crystal_pressed and not crystal_was_pressed:
            toggle_crystal()

        if obsidian_pressed and not obsidian_was_pressed:
            place_one_obsidian()

        crystal_was_pressed = crystal_pressed
        obsidian_was_pressed = obsidian_pressed

        time.sleep(0.01)

except Exception as e:
    print(f"Error: {e}")
    print("Run as Administrator!")