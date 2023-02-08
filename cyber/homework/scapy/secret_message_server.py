from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1
from typing import List
from scapy.all import *


def sniff_ports(start_port, end_port):
    filter_string = "udp and (port >= {} and port <= {})".format(start_port, end_port)
    sniff(filter=filter_string, prn=sniff_callback, store=0)
def main():
    