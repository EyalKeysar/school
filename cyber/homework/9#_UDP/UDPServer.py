import socket

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)
    while True:
        # Wait for a connection and prints the data
        print('waiting to receive message')
        data = sock.recv(1024)
        print('received %s bytes: %s' % (len(data), data))
        
if(__name__ == '__main__'):
    main()