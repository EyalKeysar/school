import socket
import os


IP = '127.0.1.1'
PORT = 80
SOCKET_TIMEOUT = 0.1

ROOT_FOLDER = './webroot'
DEFAULT_FILE = './webroot/index.html'
USABLE_REQUESTS = ['GET']
CALCULATE_NEXT = '/calculate-next'
CALCULATE_AREA = '/calculate-area'
PAGE_NOT_FOUND = 'HTTP/1.1 404 Request Time-out\r\n'.encode()


def get_file_data(filename):
    file = open(filename, 'rb')
    return file.read()


def file_in_root(wanted_file):
    for subdir, dirs, files in os.walk(ROOT_FOLDER):
        for file in files:
            print(file)
            if file == wanted_file:
                return True
    return False


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    try:
        if resource == '/':
            client_socket.send(get_file_data(ROOT_FOLDER + DEFAULT_FILE))
        elif os.path.exists(ROOT_FOLDER + resource.replace('/', '\\')):
            client_socket.send(get_file_data(ROOT_FOLDER + resource.replace('/', '\\')))
        elif resource.split('?')[0] == CALCULATE_NEXT:
            try:
                client_socket.send(str(int(resource.split('=')[1]) + 1).encode())
            except ValueError:
                client_socket.send('invalid'.encode())
        elif resource.split('?')[0] == CALCULATE_AREA:
            try:
                params = resource.split('?')[1].split('&')
                width = int(params[0].split('=')[1])
                height = int(params[1].split('=')[1])
                client_socket.send(str(width*height/2).encode())
            except ValueError:
                client_socket.send('invalid'.encode())

    except OSError:
        client_socket.send(PAGE_NOT_FOUND)


def validate_http_request(request):
    """
    Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL
    """
    request_line = request.split('\n')[0].split()

    if request_line[0] in USABLE_REQUESTS and request_line[2] == 'HTTP/1.1':

        if request_line[1] == '/' or os.path.exists(ROOT_FOLDER + request_line[1].replace('/', '\\')):
            return True, request.split()[1]

        if CALCULATE_NEXT in request_line[1]:
            return True, request.split()[1]

        if CALCULATE_AREA in request_line[1]:
            return True, request.split()[1]

    return False, ''


def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    # print('Client connected')

    while True:
        client_request = client_socket.recv(1024).decode()
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            # print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request\n')
            print(client_request)
            client_socket.send(PAGE_NOT_FOUND)
            break

    print('Closing connection')
    client_socket.close()


def main():
    # Open a socket and loop forever while waiting for clients
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print('New connection received')
            client_socket.settimeout(SOCKET_TIMEOUT)
            handle_client(client_socket)
        except socket.error:
            print('client has unexpectedly disconnected')


if __name__ == "__main__":
    # Call the main handler function
    main()
