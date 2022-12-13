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
PORT = 2230
SOCKET_TIMEOUT = 99*99
ROOT = "./webroot"
HTML_PATH = "./webroot/index.html"
text_file_types = {"js", "css"}


#Done ---------------------------------------------------------------
def get_file_data(filename):
    """ Get data from file """
    try:
        if("calculate-next" in filename):
            if("num=" in filename):
                return str((int(filename.split("num=")[-1]) + 1)).encode()
            
        elif("calculate-area" in filename):
            if("width=" in filename and "height=" in filename):
                filename = filename.split('?')[-1]
                height = filename.split("&")[0].split("=")[-1]
                width = filename.split("&")[1].split("=")[-1]
                return str(int(height)*int(width)/2).encode()
    except IndexError:
        print("filename not proprate")
        return "404".encode()

    
    try:
        filetype  = filename.split('.')[-1]
        file_pointer = None
        # reading the file data.
        
        #check for default path
        if(filename in {"", " ", "/", "//"}):
            file_pointer = HTML_PATH
        #walk in repository searching for the file.
        else:
            for root, dirs, files in os.walk(r'.\webroot'):
                for name in files:
                    if name == filename:
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
    if(request == "" or len(request) < 5):
        return False, ""
    if(request[0:4] == "GET " and r"HTTP/1.1" in request):
        current_path = request[4:request.index(r" HTTP")]
        return True, current_path
    else:
        return False, "-"

def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    found = False
    if(not resource in {"", " ", "/"}):
        for root, dirs, files in os.walk(r'.\webroot'):
            for name in files:
                if name == resource.split("/")[-1]:
                    found = True
    else:
        found = True
    filename = resource.split("/")[-1].replace('/', '')
    if(found or "calculate-next" in filename or "calculate-area" in filename):
        http_header = 'HTTP/1.1 200 OK\r\n'
    else:
        print("404 res = " + resource)
        http_header = "HTTP/1.1 404 Not Found\r\n"
    filetype = resource.split('.')[-1]

    if("calculate-next" in filename or "calculate-area" in filename):
        http_header += "Content-Type: text/plain; charset=utf-8\r\n"
    elif filetype == 'html' or resource in {"", " ", "/"}:
        http_header += "Content-Type: text/html; charset=utf-8\r\n"
    elif filetype == 'jpg':
        http_header += "Content-Type: image/jpg\r\n"
    elif filetype == 'ico':
        http_header += 'Content-Type: image/vnd.microsoft.icon\r\n'
    elif(filetype in text_file_types):
        http_header += 'Content-Type: text/' + filetype + '; charset=utf-8\r\n'
    else:
        print("file type error: " + resource.split('.')[-1])
    

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
    client_socket.send(http_response)
    return


def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')
    while True:
        # TO DO: insert code that receives client request
        client_request = client_socket.recv(1024)
        valid_http, resource = validate_http_request(client_request.decode())
        
        if(valid_http or resource == ""):
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request :' + resource)
            break
    print('Closing connection')
    client_socket.close()

def main():
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