#   Ex. 2.7 template - protocol


LENGTH_FIELD_SIZE = 4
PORT = 8820
CMD_PROTOCOL_INDEX = 0
PARAM_PROTOCOL_INDEX = 1
VALID_CMD = ["DELETE", "LS", "DIR", "COPY"]


def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters
    For example, DELETE c:\work\file.txt is good, but DELETE alone is not
    """
    cmd  = data.split(" ")[CMD_PROTOCOL_INDEX]
    if(cmd in VALID_CMD):
        param = data.split(" ")[PARAM_PROTOCOL_INDEX]
    else:
        print(" -- \nprotocol not recognize cmd :\n" + cmd +"\n -- ")
    

    # (3)
    return True


def create_msg(data):
    """
    Create a valid protocol message, with length field
    """
    length = len(str(data))
    zeros_left = 0

    if(len(str(length) < 4)):
        zeros_left = 4-len(str(length))
    for i in range(zeros_left):
        length = "0" + str(length)
    msg = length + data
    # (4)
    return msg.encode()


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """

    # (5)
    return True, "OK"


