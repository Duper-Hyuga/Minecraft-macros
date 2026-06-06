import keyboard
import time
import pyautogui
import mouse

HOTKEY = 'middle'
is_busy = False
was_pressed = False


def tap_key(key, hold_time):
    keyboard.press(key)
    time.sleep(hold_time)
    keyboard.release(key)


def pearl_macro():
    global is_busy

    if is_busy:
        return

    is_busy = True
    try:
        time.sleep(0.08)

        tap_key('ť', 0.01) #keys of hobar please change it to your own keys
        time.sleep(0.015)
        pyautogui.rightClick()

        print("Pearl used")

    except Exception as e:
        print(f"Macro error: {e}")

    finally:
        is_busy = False


print("Started.")
print("Press MOUSE3 (middle click) for one cycle")
print("Press ESC to exit\n")


while True:

    mouse_pressed = mouse.is_pressed(button=HOTKEY)

    if mouse_pressed and not was_pressed:
        pearl_macro()

    was_pressed = mouse_pressed
    time.sleep(0.005)