import socket
my_socket = socket.socket()
my_socket.connect(("localhost", 1337))
my_socket.send("some".encode())
data = my_socket.recv(1024)
print(data)
my_socket.close()