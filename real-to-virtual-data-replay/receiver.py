import socket
import subprocess
import base64

SRC_IFACE = "lowpan0"
SRC_PORT = 12345

DST_ADDR = "fe80::1"
DST_PORT = 12345
DST_IFACES = ['sensor1-pan0', 'sensor2-pan0', 'sensor3-pan0', 'sensor4-pan0']
DST_NODES = ['sensor1', 'sensor2', 'sensor3', 'sensor4']
VIRTUAL_NODES = ['fe80::1', 'fe80::2', 'fe80::3', 'fe80::4']

sock_in = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock_in.bind(("::", SRC_PORT))
sock_in.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, SRC_IFACE.encode())


while True:
    data, src = sock_in.recvfrom(2048)
    print(f"[RECV] {len(data)} bytes")

    src_ip = src[0]
    src_port = src[1]

    if src_ip not in VIRTUAL_NODES:
        print("[WARN] Unknown IP address:", src_ip)
        continue

    idx = VIRTUAL_NODES.index(src_ip)
    node = DST_NODES[idx]
    iface = DST_IFACES[idx]

    print(f"[LISTEN] {SRC_IFACE}:{SRC_PORT}")

    dst_pid = subprocess.check_output(["pgrep", "-f", f"mininet:{node}"]).decode().strip()
    b64 = base64.b64encode(data).decode()

    code = f"""
import socket, base64
payload = base64.b64decode("{b64}")
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
scope = socket.if_nametoindex("{iface}")
sock.sendto(payload, ("{DST_ADDR}", {DST_PORT}, 0, scope))
"""

    subprocess.run(["mnexec", "-a", dst_pid, "python3", "-c", code])
    print(f"[SEND] via {VIRTUAL_NODES[idx]}%{iface}")