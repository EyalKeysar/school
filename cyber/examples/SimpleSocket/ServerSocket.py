import socket
import threading
server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820))
print("Server is up and running")
server_is_active = True

while(server_is_active):
    server_socket.listen()

    (client_socket, client_address) = server_socket.accept()
    print("Client connected")
    data = client_socket.recv(1).decode()
    print("Client sent: " + data)
    data = client_socket.recv(1).decode()
    print("Client sent: " + data)
    print("end connection with: ", client_address[0])

    print("<--) Client disconnected: ", client_address[0])

client_socket.close()
server_socket.close()