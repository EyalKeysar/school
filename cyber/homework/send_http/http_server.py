# Ex 4.4 - HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules
import socket
import sys
import os

# TO DO: set constants
IP = '0.0.0.0'
PORT = 80
SOCKET_TIMEOUT = 5
ROOT = "./webroot"
HTML_PATH = "./webroot/index.html"



#Done ---------------------------------------------------------------
def get_file_data(filename):
    """ Get data from file """
    try:
        file_pointer = None
        # reading the file data.
        if(filename in {"", " ", "/", "//"}):
            file_pointer = open(HTML_PATH, "r", encoding = 'unicode_escape')
        else:
            for root, dirs, files in os.walk(r'C:\Networks\school\cyber\homework\send_http\webroot'):
                for name in files:
                    if name == filename: 
                        file_pointer = open(os.path.abspath(os.path.join(root, name)), "r", encoding = 'unicode_escape')
            if(not file_pointer):
                file_pointer = open(HTML_PATH, "r", encoding = 'unicode_escape')
                        
        file_data = file_pointer.read()
        file_pointer.close()
    except FileNotFoundError:
        print("file not found 404 = " + filename)
        file_data = None
    return file_data
# --------------------------------------------------------------------

def validate_http_request(request):
    """
    Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL
    """
    if(request == ""):
        return False, ""
    # Length validation of request.
    if(request[0:4] == "GET "):
        if(r"HTTP/1.1" in request):
            current_path = request[4:request.index(r" HTTP")] 
            return True, current_path
        else:
            return False, ""
    else:
        return False, ""

#ToDo :
def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    found = False
    for root, dirs, files in os.walk(r'C:\Networks\school\cyber\homework\send_http\webroot'):
        for name in files:
            if name == resource:
                found = True

    # TO DO: check if URL had been redirected, not available or other error code. For example:
    if(found):
        http_header = 'HTTP/1.1 200 OK\r\n'
    else:
        http_header = "HTTP/1.1 404 Not Found\r\n"

    # TO DO: extract requested file type from URL (html, jpg etc)
    filetype = resource.split('.')[-1]
    print("res = " + resource)
    if filetype == 'html' or resource == "/":
        http_header += "Content-Type: text/html\r\n"# TO DO: generate proper HTTP header
    elif filetype == 'jpg':
        http_header += "Content-Type: image/jpg\r\n"# TO DO: generate proper jpg header
        print("sent jpg")
    elif filetype == 'ico':
        http_header += 'Content-Type: image/vnd.microsoft.icon\r\n'
    else:
        print("file type error: " + resource.split('.')[-1])
        print(resource)
    # TO DO: handle all other headers

    data = get_file_data(resource.replace('/', ''))
    if(data != None):
        length = len(data)
    else:
        length = 0
    http_header += 'Content-Length: ' + len(data)  + '\r\n'
    if(data != None):
        http_response = http_header + data
    else:
        http_response = http_header
    client_socket.send(http_response.encode())


def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    while True:
        # TO DO: insert code that receives client request
        client_request = client_socket.recv(1024)
        valid_http, resource = validate_http_request(client_request)
        if(valid_http or resource == ""):
            handle_client_request(resource, client_socket)
            print("handeled")
        else:
            print('Error: Not a valid HTTP request :' + resource)
            break
    print('Closing connection')
    client_socket.close()

#Done -----------------------------------------------------------------------------------------------
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