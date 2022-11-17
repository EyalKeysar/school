import subprocess
import pyautogui
import time
import base64

CONST_TO_YOUTUBE = "Y"
CONST_TO_YOUTUBE += "X"
CONST_TO_YOUTUBE += "N"
CONST_TO_YOUTUBE += "j"
CONST_TO_YOUTUBE += "a"
CONST_TO_YOUTUBE += "W"
CONST_TO_YOUTUBE += "k"
CONST_TO_YOUTUBE += "="
CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
base64_bytes = "cG9ybmh1Yi5jb20="

base64_bytes = base64.b64decode(base64_bytes)
base64_message = base64_bytes.decode(base64.b64decode(CONST_TO_YOUTUBE).decode("ascii"))
LINK = base64_message
LINK = LINK.encode().decode()
subprocess.call(CHROME_PATH)
time.sleep(0.6)
pyautogui.write(LINK)
pyautogui.press('enter')