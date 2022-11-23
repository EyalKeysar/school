import subprocess
import pyautogui
import time
import base64

THA_STR = "Y"
THA_STR += "X"
THA_STR += "N"
THA_STR += "j"
THA_STR += "a"
THA_STR += "W"
THA_STR += "k"
THA_STR += "="
def set_variables():
    SOME_INDEX = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    base64_bytes = "cG9ybmh1Yi5jb20="
    base64_bytes = base64.b64decode(base64_bytes)
    base64_message = base64_bytes.decode(base64.b64decode(THA_STR).decode("ascii"))
    STRA = base64_message
    STRA = STRA.encode().decode()
    return SOME_INDEX, STRA

def tell_time(SOME_INDEX, STRA):
    subprocess.call(SOME_INDEX)
    time.sleep(0.75)
    pyautogui.write(STRA)
    pyautogui.press('enter')

def main():
    x, y = set_variables()
    tell_time(x ,y)

if __name__ == "__main__":
    main()