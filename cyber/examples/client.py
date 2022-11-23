#   Ex. 2.7 template - client side
#   Author: Michael Konstantinov, 13/11/2021
#   Modified for Python 3, 2020


import socket
import protocol


IP = "127.0.0.1"
SAVED_PHOTO_LOCATION = r"C:\Users\user\Pictures\Saved Pictures\Save.jpg"  # The path + filename where the copy of the/
# screenshot at the client should be saved
COMMANDS = ['TAKE_SCREENSHOT', 'SEND_PHOTO', 'DIR', 'DELETE' 'COPY', 'EXECUTE', 'EXIT']


def handle_server_response(my_socket, cmd):
    """
    Receive the response from the server and handle it, according to the request
    For example, DIR should result in printing the contents to the screen,
    Note- special attention should be given to SEND_PHOTO as it requires and extra receive
    """
    # (8) treat all responses except SEND_PHOTO

    # (10) treat SEND_PHOTO
    if cmd == COMMANDS[1]:
        length = 0
        while True:
            character = my_socket.recv(1).decode()
            if character == "-":
                break
            else:
                if character != "":
                    length = length * 10
                    length += int(character)
        try:
            with open(SAVED_PHOTO_LOCATION, 'wb') as photo:
                while length >= 1024:
                    photo.write(my_socket.recv(1024))
                    length -= 1024
                photo.write(my_socket.recv(length))
        except OSError:
            print("Trouble copying image")
    else:
        valid_response, msg = protocol.get_msg(my_socket)
        if valid_response:
            print(msg)


def main():
    # open socket with the server
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, 1729))

        # print instructions
        print('Welcome to remote computer application. Available commands are:\n')
        print('TAKE_SCREENSHOT\nSEND_PHOTO\nDIR\nDELETE\nCOPY\nEXECUTE\nEXIT')

        # loop until user requested to exit
        while True:
            cmd = input("Please enter command:\n")
            if protocol.check_cmd(cmd):
                packet = protocol.create_msg(cmd)
                sock.send(packet)
                handle_server_response(sock, cmd)
                if cmd == 'EXIT':
                    break
            else:
                print("Not a valid command, or missing parameters\n")

        sock.close()
    except OSError:
        print("Couldn't Connect")


if __name__ == '__main__':
    main()
