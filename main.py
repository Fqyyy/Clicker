import pyautogui
import threading
from pynput import keyboard

is_clicking = threading.Event()

def click_mouse():
    while is_clicking.is_set():
        pyautogui.doubleClick()

def on_press(key):
    try:
        if key == keyboard.Key.scroll_lock: #Кликер на scroll_lock/The clicker on scroll_lock
            if not is_clicking.is_set():
                is_clicking.set()
                threading.Thread(target=click_mouse, daemon=True).start()
            else:
                is_clicking.clear()
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

