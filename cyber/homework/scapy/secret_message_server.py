from scapy.sendrecv import sr1
from scapy.all import *

client_ip = "127.0.0.5"

def sniff_ports():
    filter_string = "udp and host {client_ip}"
    recived_port = sniff(filter=filter_string, count=1)
    print(recived_port)
def main():
    while True:
        sniff_ports()
        
if "__main__" == __name__:
    main()