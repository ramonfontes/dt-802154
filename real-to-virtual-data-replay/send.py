import socket
import os
import time

IFACE = "lowpan0"
DST_PORT = 12345
NUM_PACKETS = 60

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
addr = (f"fe80::10", DST_PORT, 0, socket.if_nametoindex(IFACE))

for i in range(NUM_PACKETS):
    data = os.urandom(8)
    print(f"[SEND {i+1}/60] {len(data)} bytes:", data.hex())
    sock.sendto(data, addr)
    time.sleep(1)