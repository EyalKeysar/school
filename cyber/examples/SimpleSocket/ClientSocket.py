import socket
my_socket = socket.socket()
my_socket.connect(("192.168.152.1", 8820))
my_socket.send("mtname".encode())
data = my_socket.recv(1024).decode()
print("The server sent " + data)
my_socket.close()