from scapy.all import *
import time

# Interface where real packets are captured
REAL_IFACE = "wpan0"
# Interface where packets will be forwarded (Digital Twin or another node)
SEND_IFACE = "sensor1-wpan0"

def forward_packet(pkt):
    """
    Function executed every time a packet is captured.
    You may inspect, copy, modify, or forward the packet here.
    """

    # Show useful information (optional)
    print(f"[{time.time():.4f}] Captured packet len={len(pkt)}")

    # Filter only IEEE 802.15.4 Data frames (optional)
    if pkt.haslayer(Dot15d4Data):
        print(" -> IEEE 802.15.4 Data packet detected")

    # Simple packet copy (replay)
    vpkt = pkt.copy()

    # Send the packet to the target interface
    sendp(vpkt, iface=SEND_IFACE, verbose=0)
    print(" -> Packet forwarded successfully\n")


print(f"Sniffing on {REAL_IFACE} and forwarding to {SEND_IFACE}...\n")

sniff(
    iface=REAL_IFACE,
    prn=forward_packet,
    store=False,
)
