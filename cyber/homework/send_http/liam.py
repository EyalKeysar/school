# HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes,
# log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

import socket
import time
import sys

IP = '0.0.0.0'
PORT = 80
SOCKET_TIMEOUT = 2
DEFAULT_URL = '/'
REDIRECTION_DICTIONARY = {'/source.html':'http://webroot/imgs/abstract.jpg'}
FIRST_ELEMENT = 0
SECOND_ELEMENT = 1
THIRD_ELEMENT = 2
SET_LENGTH = 1024
WWW_DIR = 'webroot' # This is the top level directory of the server
NOTFOUND = '/notfound.html'


def get_file_data(file_requested):
    file_requested = WWW_DIR+file_requested
    try:
        file_handler = open(file_requested, 'rb')
        response_content = file_handler.read()  # read content
        file_handler.close()
    except Exception as e:  # File opened/read, generate 404 page
        print("Warning, file not accessible. Issuing " \
              "response code of 404\n", e)
        response_content = None
    return response_content


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response
        and send to client
    """
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    if resource == '':
        url = DEFAULT_URL
    else:
        url = resource

    redirect = False
    if url in REDIRECTION_DICTIONARY:
        # TO DO: send 302 redirection response
        response_line1 = 'HTTP/1.1 302 Found'
        redirect = True
    elif url == '/':
        filename = '/index.html'
    else:
        filename = url

    if redirect:
        print('redirecting...')
        response_content = r'<!DOCTYPE html><html lang="en"><head>' + \
                           r'<meta charset="UTF-8"><title>Title</title>' + \
                           r'</head><body><h1> 302 Found. Please follow ' + \
                           REDIRECTION_DICTIONARY[url] + r'</h1>' + \
                           r'</body></html>'
    else:
        # TO DO: read the data from the file
        data = get_file_data(filename)
        if data is None:
            print('page not found (404)')
            response_line1 = ('HTTP/1.1 404 Not Found\r\n')
            response_content = (r'<!DOCTYPE html><html lang="en"><head>' + \
                               r'<meta charset="UTF-8"><title>Title</title>' + \
                               r'</head><body><h1> This is page 404 </h1>' + \
                               r'</body></html>')
        else:
            response_line1 = 'HTTP/1.1 200 OK\r\n'
            response_content = data

    length = len(response_content)
    header = 'content-length:' + str(length) + '\r\n\r\n'
    http_response = response_line1 + header + response_content
    print("SENT:\n" + http_response)
    client_socket.send(http_response.encode())


def validate_http_request(request):
    """ Check if request is a valid HTTP request and
        returns TRUE / FALSE and the requested URL
    """
    request_line1 = request[:request.find('\n')]
    parsed_request = request_line1.split()
    if len(parsed_request) != 3:
        print("nonvalid (< 3): " + request)
        return False, ''
    request_type = parsed_request[FIRST_ELEMENT]
    request_url = parsed_request[SECOND_ELEMENT]
    request_protocol = parsed_request[THIRD_ELEMENT]
    if request_type != 'GET' or request_protocol != 'HTTP/1.1':
        print("nonvalid: " + request)
        return False, ''
    return True, request_url


def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP,
        calls function to handle the requests
    """
    print('Client connected')
    while True:
        # TO DO: insert code that receives client request
        client_request = client_socket.recv(SET_LENGTH)  # receive data from client
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
        else:
            print('Error: Not a valid HTTP request')
            break
    print('Closing connection')
    client_socket.close()


def main():
    # Open a socket and loop forever while waiting for clients
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(10)
    print("Listening for connections on port %d" % PORT)

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        handle_client(client_socket)


if _name_ == "_main_":
    # Call the main handler function
    main()