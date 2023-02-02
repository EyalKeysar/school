from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1

def main():
    domain = input("domain: ")
    dns_req = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=domain))
    answer = sr1(dns_req, verbose=0)
    
    if(answer[DNS].ancount > 0):
        for i in range(answer[DNS].ancount):
            print("IP: ", answer[DNS].an[i].rdata)

if "__main__" == __name__:
    main()