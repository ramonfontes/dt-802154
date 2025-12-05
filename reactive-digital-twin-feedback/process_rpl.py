import sys
import socket
import struct

ICMPV6 = 58
RPL_DIO_TYPE = 155

ROOT = "fe80::1"
OUTPUT =  sys.argv[1]
iface = sys.argv[2]

# Raw ICMPv6 socket for capturing RPL DIO messages
sock = socket.socket(socket.AF_INET6, socket.SOCK_RAW, ICMPV6)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, iface.encode())

print("[INFO] Listening for RPL DIO messages on interface:", iface)

# ----- Topology dictionary: node -> { rank, parent } -----
topology = {}

# Function to extract Rank + DODAGID (fixed DIO header offsets)
def parse_dio(payload):

    if len(payload) < 24:
        return None, None

    rpl_instance = payload[0]
    version = payload[1]
    rank = struct.unpack("!H", payload[2:4])[0]
    dodagid = socket.inet_ntop(socket.AF_INET6, payload[6:22])

    return rank, dodagid


def save_topology_file():
    """Save only child -> parent pairs to topology.txt"""
    with open(OUTPUT, "w") as f:
        for node, info in topology.items():
            if node == ROOT:
                continue
            f.write(f"{node} {info['parent']}\n")


while True:
    raw, addr = sock.recvfrom(2048)
    src_ip = addr[0]

    # Byte 0 = ICMPv6 Type
    icmp_type = raw[0]
    if icmp_type != RPL_DIO_TYPE:
        continue

    # Skip the IPv6 header (first 40 bytes) to get the DIO payload
    dio_payload = raw[4:]

    rank, dagid = parse_dio(dio_payload)

    if rank is None or rank is 0:
        continue

    print(f"\n[RECV] RPL DIO from {src_ip}")

    # ----- Update Topology -----

    # Ensure root exists
    topology.setdefault(ROOT, {"rank": 1, "parent": None})

    # The sender of the DIO has rank = rank
    topology[src_ip] = {
        "rank": rank,
        "parent": None  # will be computed below
    }

    # Find the best parent: any node with lower rank
    parent_candidate = None
    best_rank = 999999

    for node, info in topology.items():
        if node == src_ip:
            continue
        if info["rank"] < rank and info["rank"] < best_rank:
            parent_candidate = node
            best_rank = info["rank"]

    topology[src_ip]["parent"] = parent_candidate

    # Save file every update
    save_topology_file()

    # ----- Print current topology -----
    print("\n=== RPL TOPOLOGY ===")
    for node, info in sorted(topology.items(), key=lambda x: x[1]["rank"]):
        print(f"Node {node:20} → Parent {info['parent']}")