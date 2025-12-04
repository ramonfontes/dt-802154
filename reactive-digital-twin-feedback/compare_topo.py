import os
import socket
import subprocess
import time

VIRTUAL_FILE = "virtual_topo.txt"
PHY_FILE = "phy_topo.txt"
CHECK_INTERVAL = 5   # check every 5 seconds
STABLE_TIME = 30     # time required to consider topology stable

def read_topo(file_path):
    """Read topology file and return a set of child-parent pairs"""
    try:
        with open(file_path, "r") as f:
            lines = f.read().splitlines()
            return set(lines)
    except FileNotFoundError:
        return set()

stable_counter = 0

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
    virtual_topo = read_topo(VIRTUAL_FILE)
    phy_topo = read_topo(PHY_FILE)

    if virtual_topo == phy_topo:
        stable_counter += CHECK_INTERVAL
        print(f"[INFO] Topologies match for {stable_counter} seconds")
    else:
        stable_counter = 0
        print("[INFO] Topologies differ")

    if stable_counter >= STABLE_TIME:
        print("[TRIGGER] Topology stable for 30s - we can now adjust the real network Trickle")
        # Here you can call the function to adjust the trickle
        stable_counter = 0  # optional, if you want to reset the counter

        IFACE = "lowpan0"
        DST_PORT = 12345

        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        addr = (f"fe80::2", DST_PORT, 0, socket.if_nametoindex(IFACE))

        data = os.urandom(8)
        print(f"[SEND] {len(data)} bytes:", data.hex())
        sock.sendto(data, addr)

        addr = (f"fe80::3", DST_PORT, 0, socket.if_nametoindex(IFACE))
        print(f"[SEND] {len(data)} bytes:", data.hex())
        sock.sendto(data, addr)

        update_trickle_and_reload(30)

    time.sleep(CHECK_INTERVAL)
