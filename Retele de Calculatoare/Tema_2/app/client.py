import sys
from scapy.all import IP, UDP, Raw, send

if len(sys.argv) != 2:
    print("Utilizare: python client.py <adresa_server>")
    sys.exit(1)

SERVER_IP = sys.argv[1]
SERVER_PORT = 9999
MESSAGE = "Salut de la Stefan"
IP_REAL = "172.18.0.3"
IP_FICTIV = "10.20.30.40"

try:
    packet_real = IP(src=IP_REAL, dst=SERVER_IP) / UDP(sport=12345, dport=SERVER_PORT) / Raw(load=MESSAGE)
    print("Trimit pachet UDP cu IP real...")
    send(packet_real, verbose=True)

    packet_spoofed = IP(src=IP_FICTIV, dst=SERVER_IP) / UDP(sport=12345, dport=SERVER_PORT) / Raw(load=MESSAGE)
    print("Trimit pachet UDP cu IP fictiv...")
    send(packet_spoofed, verbose=True)

except Exception as e:
    print(f"Eroare la trimiterea pachetului: {e}")