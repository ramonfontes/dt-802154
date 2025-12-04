import socket
import subprocess

SRC_IFACE = "lowpan0"
SRC_PORT = 12345

sock_in = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock_in.bind(("::", SRC_PORT))
sock_in.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, SRC_IFACE.encode())


def update_trickle_and_reload(value):
    """Write new trickle value and send SIGUSR1 to rpld."""

    # Write into the file
    with open("/tmp/trickle.conf", "w") as f:
        f.write(f"trickle_t={value}\n")

    print(f"[UPDATE] trickle_t set to {value} in /tmp/trickle.conf")

    # Send SIGUSR1 signal
    try:
        rpld_pid = subprocess.check_output(["pidof", "rpld"]).decode().strip()
        subprocess.run(["kill", "-SIGUSR1", rpld_pid])
        print(f"[SIGNAL] Sent SIGUSR1 to rpld (pid={rpld_pid})")
    except subprocess.CalledProcessError:
        print("[ERROR] rpld is not running!")


while True:
    data, src = sock_in.recvfrom(2048)
    print(f"[RECV] {len(data)} bytes from {src[0]}")
    update_trickle_and_reload(30)

