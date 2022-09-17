import socket
import threading
server_socket = socket.socket()
server_socket.bind(("192.168.152.1", 8820))
print("Server is up and running")
server_is_active = True

while(server_is_active):
    server_socket.listen()

    (client_socket, client_address) = server_socket.accept()
    print("Client connected")
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)
    reply = "Hello " + data
    client_socket.send(reply.encode())
    print("end connection with: ", client_address[0])

def HandleClient(client_socket, client_address):
    print("-->) Client connected: ", client_address[0])

    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)
    reply = "Hello " + data
    client_socket.send(reply.encode())

    print("<--) Client disconnected: ", client_address[0])

client_socket.close()
server_socket.close()