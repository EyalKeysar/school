import socket
from socket import gethostbyname
from scapy.all import *
import sys

FROM = 20
TO = 1024

SRC_PORT = 2435
hostn = "172.16.10.58"
dest = "www.google.com"

for i in range(FROM, TO):
    syn_packet = IP(src=hostn, dst=dest) / TCP(sport=SRC_PORT, dport=i, flags='S', seq=1)
    syn_ack_packet = sr1(syn_packet, timeout=1)

    if syn_ack_packet and syn_ack_packet.haslayer(TCP) and syn_ack_packet[TCP].flags == 'SA':
        print('sec: ' + str(i))
    else:
        print('failed: ' + str(i))
