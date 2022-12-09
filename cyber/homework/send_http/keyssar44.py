# Ex 4.4 - HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules
import socket
import sys
import os
import cv2
# TO DO: set constants
IP = '0.0.0.0'
PORT = 2230
SOCKET_TIMEOUT = 5
ROOT = "./webroot"
HTML_PATH = "./webroot/index.html"



#Done ---------------------------------------------------------------
def get_file_data(filename):
    """ Get data from file """
    print("getting = " + filename)
    filetype  = filename.split('.')[-1]
    print(filetype)
    try:
        file_pointer = None
        # reading the file data.
        
        #check for default path
        if(filename in {"", " ", "/", "//"}):
            file_pointer = HTML_PATH
        #walk in repository searching for the file.
        else:
            for root, dirs, files in os.walk(r'.\webroot'):
                for name in files:
                    print("name = " + name)
                    print("name to find = " + filename)
                    if name == filename:
                        print("ok")
                        file_pointer = os.path.abspath(os.path.join(root, name))
        #if file found
        if(file_pointer != None):
            with open(file_pointer, 'rb') as f:
                if(filetype == 'jpg'):
                    return f.read()
                else:
                    return f.read()
        else:
            return "404".encode()
    except FileNotFoundError:
        print("file not found 404 = " + filename)
        return "404".encode()
# --------------------------------------------------------------------

def validate_http_request(request):
    """
    Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL
    """
    if(request == ""):
        print("somelse")
        return False, ""
    # Length validation of request.
    if(request[0:4] == "GET "):
        if(r"HTTP/1.1" in request):
            current_path = request[4:request.index(r" HTTP")] 
            print("valid + " + current_path)
            return True, current_path
        else:
            print("nonval " + request)
            return False, "-"
    else:
        print("nonval " + request)
        return False, "-"

#ToDo :
def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    found = False
    if(not resource in {"", " ", "/"}):
        for root, dirs, files in os.walk(r'.\webroot'):
            for name in files:
                if name == resource.split("/")[-1]:
                    found = True
    else:
        found = True
    # TO DO: check if URL had been redirected, not available or other error code. For example:
    if(found):
        http_header = 'HTTP/1.1 200 OK\r\n'
    else:
        print("404 res = " + resource)
        http_header = "HTTP/1.1 404 Not Found\r\n"

    # TO DO: extract requested file type from URL (html, jpg etc)
    filetype = resource.split('.')[-1]
    if filetype == 'html' or resource in {"", " ", "/"}:
        http_header += "Content-Type: text/html; charset=utf-8\r\n"# TO DO: generate proper HTTP header
    elif filetype == 'jpg':
        http_header += "Content-Type: image/jpg\r\n"# TO DO: generate proper jpg header
        print("sent jpg")
    elif filetype == 'ico':
        http_header += 'Content-Type: image/vnd.microsoft.icon\r\n'
    elif(filetype == "css"):
        http_header += 'Content-Type: text/css\r\n'
    else:
        print("file type error: " + resource.split('.')[-1])
    # TO DO: handle all other headers
    

    data = get_file_data(resource.split("/")[-1].replace('/', ''))
    if(data != None):
        length = len(data)
    else:
        length = 0
    http_header += 'Content-Length: ' + str(len(data))  + '\r\n\r\n'
    if(data != None):
        http_response = http_header.encode() + data
    else:
        http_response = http_header.encode()
    print("sent")
    client_socket.send(http_response)
    return


def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    while True:
        # TO DO: insert code that receives client request
        client_request = client_socket.recv(1024)
        print("req = " +client_request.decode())
        valid_http, resource = validate_http_request(client_request.decode())
        
        if(valid_http or resource == ""):
            print("res = " + resource)
            handle_client_request(resource, client_socket)
            print("handeled")
            break
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