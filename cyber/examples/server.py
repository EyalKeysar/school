#   Ex. 2.7 template - server side
#   Author: Michael Konstantinov, 13/11/2021
#   Modified for Python 3, 2020
import os.path
import shutil
import socket
import subprocess
import protocol
import pyautogui
COMMANDS = ['TAKE_SCREENSHOT', 'SEND_PHOTO', 'DIR', 'DELETE', 'COPY', 'EXECUTE', 'EXIT']

IP = "127.0.0.1"
PHOTO_PATH = r"C:\Users\user\Pictures\Saved Pictures\SS.jpg"
# The path + filename where the screenshot at the server should be saved


def connect_to_client():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 1729))
    server_socket.listen(1)
    client_socket, client_adress = server_socket.accept()
    print("connected")
    return client_socket


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
    if not protocol.check_cmd(cmd):
        return False, "", ""
    # Then make sure the params are valid
    parts = cmd.split(" ", 1)
    if parts[0] == COMMANDS[2]:
        if os.path.isdir(parts[1]):
            return True, parts[0], parts[1]
    elif parts[0] == COMMANDS[3]:
        if os.path.isfile(parts[1]):
            return True, parts[0], parts[1]
    elif parts[0] == COMMANDS[4]:
        file1 = ""
        while not os.path.isfile(file1):
            file1 += parts[1][0]
            parts[1] = parts[1][1:]
            if len(parts[1]) == 0:
                break
        if len(parts[1]) == 0:
            if parts[1][0] == " ":
                parts[1] = parts[1][1:]
        if os.path.isfile(file1):
            return True, parts[0], [file1, parts[1]]
    elif parts[0] == COMMANDS[5]:
        if shutil.which(parts[1]) is not None:
            return True, parts[0], parts[1]
    elif parts[0] == COMMANDS[0] or parts[0] == COMMANDS[1] or parts[0] == COMMANDS[6]:
        return True, parts[0], ""
    return False, "", ""
    # (6)


def handle_client_request(command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory
    Note: in case of SEND_PHOTO, only the length of the file will be sent

    Returns:
        response: the requested data

    """
    try:
        if command == COMMANDS[0]:
            image = pyautogui.screenshot()
            try:
                image.save(PHOTO_PATH)
            except FileNotFoundError:
                return "File path not found for saving screenshot"
        elif command == COMMANDS[1]:
            try:
                return str(os.path.getsize(PHOTO_PATH)) + "-"
            except FileNotFoundError:
                return "File path not found for saving screenshot"
        elif command == COMMANDS[2]:
            try:
                files_list = os.listdir(params)
                msg = ""
                for file in files_list:
                    msg += file + '\n'
                return msg
            except OSError:
                return "Couldn't open directory"
        elif command == COMMANDS[3]:
            try:
                os.remove(params)
            except OSError:
                return "Couldn't remove file"
        elif command == COMMANDS[4]:
            try:
                shutil.copy(params[0], params[1])
            except shutil.SameFileError:
                return "Files are the same"
            except PermissionError:
                return "Permission denied."
            except OSError:
                return "Error copying file"
        elif command == COMMANDS[5]:
            try:
                subprocess.run([params])
            except OSError:
                return "Couldn't run program"
    except PermissionError:
        return "Permission denied"
    response = 'OK'
    return response


def main():
    # open socket with client
    client_socket = connect_to_client()
    # (1)
    try:
        # handle requests until user asks to exit
        while True:
            # Check if protocol is OK, e.g. length field OK
            valid_protocol, cmd = protocol.get_msg(client_socket)
            if valid_protocol:
                # Check if params are good, e.g. correct number of params, file name exists
                valid_cmd, command, params = check_client_request(cmd)
                if valid_cmd:
                    msg = handle_client_request(command, params)

                    if command == COMMANDS[1]:
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
        print("Closing connection")
    except ConnectionResetError:
        print("Connection Lost")


if __name__ == '__main__':
    main()
