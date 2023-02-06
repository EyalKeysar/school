import socket
import base64
SERVER_IP = "mail.gmx.com"
MAIL_ADDR = "frusta@gmx.com"
DATA = "Waka Waka\nWaka Waka"
PORT = 25


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    init_sock(client_socket)
    start(client_socket)
    
def init_sock(sock: socket):
    sock.connect((SERVER_IP, PORT))
    
def start(sock):
    sock.send(b"EHLO")
    data = sock.recv(1024)
    data = data.decode()
    if(data[0:3] == "220"):
        print("first ehlo")
        sock.send(b"AUTH PLAIN AGZydXN0YUBnbXguY29tAFBhc3N3b3JkMSE=")
        nxt = sock.recv(1024)
        nxt = nxt.decode()
        print(nxt)
    else:
        print("status code unknown: \n" + data[0:3])
    

if __name__ == "__main__":
    main()