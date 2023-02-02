from scapy.all import *

# define the DNS query packet
dns_query = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.google.com"))

# send the packet
send(dns_query)

# receive the response
dns_response = sniff(filter="udp and src port 53",count=1)

# extract and print the DNS response information
print(dns_response[0][DNS].summary())
