import socket
import pyautogui

def main():
    host = '127.0.0.1'
    port = 55555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print("[+] Server Started!")
    conn, addr = s.accept()
    print("[+] Connected to ",addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == "stop":
            break
        print("Received from user: " + str(data))
        pyautogui.moveRel(int(data.split(',')[0]), int(data.split(',')[1]))
    conn.close()
    s.close()

if __name__ == '__main__':
    main()
