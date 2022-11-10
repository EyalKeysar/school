import socket
my_socket = socket.socket()
my_socket.connect(("127.0.0.8", 8820))
my_socket.send("some".encode())
my_socket.close()