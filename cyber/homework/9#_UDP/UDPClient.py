import socket

serverIP = '172.16.16.202'
dest_port = 8820
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto(b'kbjbkljbl', (serverIP, dest_port))