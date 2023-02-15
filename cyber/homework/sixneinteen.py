import socket
from scapy.all import *

syn_seg = TCP(dport=80, seq=123, flags='S')
