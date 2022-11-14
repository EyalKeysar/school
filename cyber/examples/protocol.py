#   Ex. 2.7 template - protocol
import sys

LENGTH_FIELD_SIZE = 4
PORT = 1729
COMMANDS = ['TAKE_SCREENSHOT', 'SEND_PHOTO', 'DIR', 'DELETE', 'COPY', 'EXECUTE', 'EXIT']


def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters
    For example, DELETE c:\work\file.txt is good, but DELETE alone is not
    """
    for i in range(len(COMMANDS)):
        if data.find(COMMANDS[i]) != -1:

            if i == 0 or i == 6 or i == 1:
                return data == COMMANDS[i]
            else:
                data = data.replace(COMMANDS[i] + " ", "")
                data = data.replace(COMMANDS[i], "")
                if data != "":
                    return True
    # (3)
    return False


def create_msg(data):
    """
    Create a valid protocol message, with length field
    """
    if type(data) is str:
        size = str(len(data))
    else:
        size = str(sys.getsizeof(data))
    msg = size + "-" + data
    return msg.encode()


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    length = 0
    while True:
        character = my_socket.recv(1).decode()
        if character == "-":
            break
        elif not character.isnumeric:
            return False, "Error"
        else:
            if character != "":
                length = length * 10
                length += int(character)
    msg = my_socket.recv(length).decode()
    return True, msg
