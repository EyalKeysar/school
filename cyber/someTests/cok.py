import pyautogui
import keyboard
import time
while(not keyboard.is_pressed("q")):
    while(not keyboard.is_pressed("a")):
        pyautogui.click(150, 500)
    time.sleep(15)
    