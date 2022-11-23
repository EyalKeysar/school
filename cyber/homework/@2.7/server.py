#   Ex. 2.7 template - server side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020

import socket
import os
import protocol
import pyautogui
import subprocess
import shutil

IP = "0.0.0.0"
PHOTO_PATH = r"C:\Networks\school\cyber\homework\@2.7\scshot.png" # The path + filename where the screenshot at the server should be saved
CMD_PROTOCOL_INDEX = 0
PARAM_PROTOCOL_INDEX = 1
SEC_PARAM_INDEX = 2
VALID_CMD = ["DIR", "DELETE", "COPY", "EXECUTE", "TAKE_SCREENSHOT"]
ZERO_PARAM_CMD = ["TAKE_SCREENSHOT"]
ONE_PARAM_CMD = ["DIR", "EXECUTE", "DELETE"]
TWO_PARAM_CMD = ["COPY"]

def take_cur_screen():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(PHOTO_PATH)
    return str(open(PHOTO_PATH, "rb").read())

def check_client_request(cmd):
    """
    Break cmd to command and parameters
    Check if the command and params are good.
    For example, the filename to be copied actually exists
    Returns:
        valid: True/False
        command: The requested cmd (ex. "DIR")
        params: List of the cmd params (ex. ["c:\\cyber"])
    """
    # Use protocol.check_cmd first
    if(not protocol.check_cmd(cmd)):
        try:
            return False, cmd.split(" ")[CMD_PROTOCOL_INDEX], cmd.split(" ")[1:]
        except:
            return False, "nonDef", []
    # Then make sure the params are valid
    try:
        cmdlst= cmd.split(" ")
        if(cmdlst[CMD_PROTOCOL_INDEX] in ONE_PARAM_CMD):
            if(os.path.exists(cmdlst[PARAM_PROTOCOL_INDEX])):
                return True, cmdlst[CMD_PROTOCOL_INDEX], cmdlst[PARAM_PROTOCOL_INDEX]
            else:
                print("path not exist " + cmdlst[PARAM_PROTOCOL_INDEX])
                return False, cmdlst[CMD_PROTOCOL_INDEX], ["not Exists"]
        if(cmdlst[CMD_PROTOCOL_INDEX] in TWO_PARAM_CMD):
            if(os.path.exists(cmdlst[PARAM_PROTOCOL_INDEX]) and os.path.exists(os.path.exists(cmdlst[SEC_PARAM_INDEX]))):
                return True, cmdlst[CMD_PROTOCOL_INDEX], cmdlst[PARAM_PROTOCOL_INDEX:]
            else:
                print("path not exist " + cmdlst[PARAM_PROTOCOL_INDEX] + " and " + cmdlst[SEC_PARAM_INDEX])
                return False, cmdlst[CMD_PROTOCOL_INDEX], ["not Exists"]
    except:
        return False, "NONE", []


def handle_client_request(command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory
    Note: in case of SEND_PHOTO, only the length of the file will be sent

    Returns:
        response: the requested data

    """

    # (7)
    if(command == "DIR"):
        response = os.listdir(params[0])
    elif(command == "EXECUTE"):
        subprocess.call(params[0], shell=True)
        response = "OK"
    elif(command == "DELETE"):
        os.remove(params[0])
        response = "OK"
    elif(command == "COPY"):
        shutil.copyfile(params[0], params[1])
        response = "OK"
    elif(command == "TAKE_SCREENSHOT"):
        response = take_cur_screen()
        

    return response
def connect_to_client():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8820))
    server_socket.listen(1)
    client_socket, client_adress = server_socket.accept()
    print("connected")
    return client_socket

def main():
    # open socket with client
    client_socket = connect_to_client()
    # (1)
    try:
        # handle requests until user asks to exit
        while True: # Check if protocol is OK, e.g. length field OK
                valid_protocol, cmd = protocol.get_msg(client_socket)
                if valid_protocol:
                    # Check if params are good, e.g. correct number of params, file name exists
                    valid_cmd, command, params = check_client_request(cmd)
                    if valid_cmd:
                        msg = handle_client_request(command, params)

                        if command == "TAKE_SCREENSHOT":
                            client_socket.send(msg.encode())
                            with open(PHOTO_PATH, 'rb') as photo:
                                length = os.path.getsize(PHOTO_PATH)
                                while length >= 1024:
                                    client_socket.send(photo.read(1024))
                                    length -= 1024
                                client_socket.send(photo.read(length))
                        else:

                            # add length field using "create_msg"
                            msg = protocol.create_msg(msg)
                            # send to client
                            client_socket.send(msg)
                        if command == 'EXIT':
                            break
                    else:
                        # prepare proper error to client
                        response = 'Bad command or parameters'
                        # send to client
                        msg = protocol.create_msg(response)
                        client_socket.send(msg)

                else:
                    # prepare proper error to client
                    response = 'Packet not according to protocol'
                    # send to client
                    msg = protocol.create_msg(response)
                    client_socket.send(msg)
                    # Attempt to clean garbage from socket
                    client_socket.recv(1024)
            # close sockets
    except ConnectionResetError:
        print("Connection Lost")


if __name__ == '__main__':
    main()
