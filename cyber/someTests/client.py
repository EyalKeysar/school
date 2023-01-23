import socket
import pyautogui

def main():
    host = '127.0.0.1'
    port = 55555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        x, y = pyautogui.position()
        positionStr = str(x) + "," + str(y)
        s.sendall(positionStr.encode())
        if keyboard.is_pressed('q'): 
            s.sendall('stop'.encode())
            break

if __name__ == '__main__':
    main()
