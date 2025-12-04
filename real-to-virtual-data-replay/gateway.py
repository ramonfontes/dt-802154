import socket

SRC_IFACE = "sensor1-pan0"
SRC_PORT = 12345

sock_in = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock_in.bind(("::", SRC_PORT))
sock_in.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, SRC_IFACE.encode())


while True:
    data, src = sock_in.recvfrom(2048)
    print(f"[RECV] {len(data)} bytes")