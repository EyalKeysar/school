"""EX 2.6 protocol implementation
   Author:
   Date:
"""

LENGTH_FIELD_SIZE = 2
PORT = 8820


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    valid_data = ["RAND", "WHORU", "TIME", "EXIT"]
    if(data in valid_data):
        return True
    else: 
        return False


def create_msg(data):
    """Create a valid protocol message, with length field"""
    length = len(data)
    if(length < 10):
        length = "0" + str(length)
    new_data = str(length) + data
    return new_data


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    data = my_socket.recv(2)
    try:
        length = int(data)
        msg = my_socket.recv(length).decode()
    except ValueError:
        return False, "Error"
    return True, msg
