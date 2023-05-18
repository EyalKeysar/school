from threading import Thread
import socket
import random

HOST = 'localhost'
PORT = 1337
ADDR = (HOST, PORT)

def handle_client(client_socket, address):
    """ Handle a client connection, by reciving 1024 and return what he send """
    data = client_socket.recv(1024).decode()
    print("recived from client: " + data)
    client_socket.send((data + "ema shelh").encode())

def main():
    """ Start a socket Multiuser server with threading """
    print(" ~| (*) --- STARTING SERVER --- (*) |~")
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(ADDR)
    while True:
        socket_server.listen(5)
        client_socket, address = socket_server.accept()
        print("== client connected ==")
        handle_thread = Thread(target=handle_client, args=(client_socket, address))
        handle_thread.start()
        print("== client handling ==") 
        handle_thread.join()
        print("== client handled ==")

if __name__ == "__main__":
    main()