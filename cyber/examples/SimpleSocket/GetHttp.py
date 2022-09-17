# Ex 4.4 - HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules
import socket
#from urllib import request

# TO DO: set constants
IP = '0.0.0.0'
PORT = 80
SOCKET_TIMEOUT = 0.1
DEFAULT_URL = "\Networks\webroot\index.html"
filetype = "html"

def get_file_data(filename):
    """ Get data from file """
    
    return


def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    
    
    if resource == '':
        url = DEFAULT_URL
    else:
        url = resource

    # TO DO: extract requested file tupe from URL (html, jpg etc)
    if filetype == 'html':
        http_header = "HTTP/1.1 200 OK\r\n"# TO DO: generate proper HTTP header
    # TO DO: handle all other headers

    # TO DO: read the data from the file
    data = get_file_data(url)
    http_response = http_header + data
    client_socket.send(http_response.encode())
    

def validate_http_request(request):
    """
    Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL
    """
    is_http_get = False
    if(request[0:3] == "GET" and "HTTP/1.1\r\n" in request):
        is_http_get = True
        scrapped_url = request[4:request.find("HTTP/1.1\r\n")]
    # TO DO: write function
    return is_http_get, "Error in protocol detection."

def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    client_socket.send(FIXED_RESPONSE.encode())
    
    while True:
        # TO DO: insert code that receives client request
        # ...
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request')
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
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()