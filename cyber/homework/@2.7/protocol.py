#   Ex. 2.7 template - protocol


LENGTH_FIELD_SIZE = 4
PORT = 8820
CMD_PROTOCOL_INDEX = 0
PARAM_PROTOCOL_INDEX = 1
SEC_PARAM_INDEX = 2
VALID_CMD = ["DIR", "DELETE", "COPY", "EXECUTE", "TAKE_SCREENSHOT"]
ZERO_PARAM_CMD = ["TAKE_SCREENSHOT"]
ONE_PARAM_CMD = ["DIR", "EXECUTE", "DELETE"]
TWO_PARAM_CMD = ["COPY"]

def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters
    For example, DELETE c:\work\file.txt is good, but DELETE alone is not
    """
    try:
        cmd  = data.split(" ")[CMD_PROTOCOL_INDEX]
        if(cmd in ZERO_PARAM_CMD):
            return True
        elif(cmd in ONE_PARAM_CMD):
            data.split(" ")[PARAM_PROTOCOL_INDEX]
            return True
        elif(cmd in TWO_PARAM_CMD):
            data.split(" ")[PARAM_PROTOCOL_INDEX]
            data.split(" ")[SEC_PARAM_INDEX]
            return True
        else:
            print(" -- \nprotocol not recognize cmd :\n" + cmd +"\n -- ")
            return False
    except:
        print("not enough params")
        return False
    # (3)


def create_msg(data):
    """
    Create a valid protocol message, with length field
    """
    if(len(data) < 10000):
        msg = len(data) + "#" + data
    return msg.encode()


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    size = ""
    cur_char = " "
    while(cur_char != "#"):
        size = size + cur_char
        cur_char = my_socket.recv(1).decode()
    try:
        size = int(size)
        data = my_socket.recv(size).decode()
        return True, data
    except:
        print("the size field not by protocol")
        return False, "Error"
    # (5)
    return True, "OK"