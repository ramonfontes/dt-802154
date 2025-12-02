from scapy.all import *

REAL_IFACE = "wpan1"    # interface receiving 6LoWPAN / IPv6 packets

# RPL ICMPv6 type and message codes
ICMPV6_RPL_TYPE = 155

RPL_MESSAGES = {
    0x00: "DIS",
    0x01: "DIO",
    0x02: "DAO",
    0x03: "DAO-ACK"
}

def is_rpl(pkt):
    """
    Checks whether a packet is an RPL ICMPv6 control message.
    """

    print(pkt)
    if not pkt.haslayer(ICMPv6RPL):
        return False

    rpl = pkt[ICMPv6RPL]

    # Only accept valid RPL control messages
    return rpl.icmpv6_rpl_code in RPL_MESSAGES


def handle_rpl(pkt):
    """
    Called whenever an RPL message is detected.
    """

    rpl = pkt[ICMPv6RPL]
    msg_type = RPL_MESSAGES.get(rpl.icmpv6_rpl_code, "UNKNOWN")

    print("===========================================")
    print(f"RPL message detected: {msg_type}")
    print(f"Code: {rpl.icmpv6_rpl_code}")
    print(f"ICMPv6 type: {ICMPV6_RPL_TYPE}")
 
    # Show IPv6 src/dst if available
    if pkt.haslayer(IPv6):
        print(f"Source:      {pkt[IPv6].src}")
        print(f"Destination: {pkt[IPv6].dst}")

    print(f"Full packet:")
    pkt.show()
    print("===========================================\n")


print(f"Sniffing RPL messages on {REAL_IFACE}...\n")

sniff(
    iface=REAL_IFACE,
    store=False,
    prn=lambda pkt: handle_rpl(pkt) if is_rpl(pkt) else None,
)
