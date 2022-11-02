"""EX 2.6 server implementation
   Author:
   Date:
"""

from pydoc import cli
import socket
import protocol
import random
from datetime import datetime

server_name = "Eyal's server"

def create_server_rsp(cmd):
    """Based on the command, create a proper response"""
    if(cmd == "TIME"):
        resp = datetime.now()
    elif(cmd == "WHORU"):
        resp = server_name
    elif(cmd == "RAND"):
        resp = str(random.randrange(10))
    elif(cmd == "EXIT"):
        resp = "exit"
    else:
        resp = "-0-"
    return resp


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol
        valid_msg, cmd = protocol.get_msg(client_socket)
        if valid_msg:
            # 1. Print received message
            print("msg recv : " + cmd)
            # 2. Check if the command is valid
            # 3. If valid command - create response
            if(protocol.check_cmd(cmd)):
                response = create_server_rsp(cmd)
            else:
                response = "Wrong command"
        else:
            response = "Wrong protocol"
            client_socket.recv(1024)  # Attempt to empty the socket from possible garbage
        # Handle EXIT command, no need to respond to the client
        if(response == "exit"):
            print("exiting")
            client_socket.close()
            break
        else:
            client_socket.send(protocol.create_msg(str(response)).encode())
        # Send response to the client
    print("Closing\n")
    # Close sockets


if __name__ == "__main__":
    main()
