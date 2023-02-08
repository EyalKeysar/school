from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1
from typing import List

def text_to_ascii(text) -> List[int]:
    return [ord(c) for c in text]

def send_UDP(ascii: List[int]) -> None:
    for i in range(len(ascii)):
        sr1(IP(dst='127.0.0.3')/UDP(dport=ascii[i]), verbose=0)

def main():
    text = input("text: ")
    send_UDP(text_to_ascii(text))
    
if "__main__" == __name__:
    main()