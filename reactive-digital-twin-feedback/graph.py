from scapy.all import *
import matplotlib.pyplot as plt


def fill_missing_with_zero(times, counts):
    if not times:
        return [], []

    t_min = min(times)
    t_max = max(times)

    # Cria série contínua
    full_times = list(range(t_min, t_max + 1))
    full_counts = []

    # Prepara dicionário para lookup
    d = dict(zip(times, counts))

    for t in full_times:
        full_counts.append(d.get(t, 0))

    return full_times, full_counts


def pps_from_pcap_no_tcp(pcap_path):
    """
    Compute packets-per-second (PPS) while ignoring TCP packets.
    Returns normalized timestamps (starting at 0) and packet counts.
    """
    pkts = rdpcap(pcap_path)

    pps = {}
    base_time = None

    for pkt in pkts:

        # Establish reference time (t = 0 at first packet)
        if base_time is None:
            base_time = pkt.time

        # Normalize timestamp
        t = int(pkt.time - base_time)

        pps[t] = pps.get(t, 0) + 1

    # Sort timestamps
    times = sorted(pps.keys())
    counts = [pps[t] for t in times]

    return times, counts


# ============
# Input PCAP files
# ============

pcap1 = "virtual.pcap"
pcap2 = "phy.pcap"

t1, c1 = pps_from_pcap_no_tcp(pcap1)
t2, c2 = pps_from_pcap_no_tcp(pcap2)

t1, c1 = fill_missing_with_zero(t1, c1)
t2, c2 = fill_missing_with_zero(t2, c2)

# ============
# Plot
# ============

plt.figure(figsize=(12, 5))

plt.plot(t1, c1, label="Virtual")
plt.plot(t2, c2, label="Physical")

plt.title("Packets Per Second (PPS)")
plt.xlabel("Time (s)")
plt.ylabel("Packet Count")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("graph.eps", format="eps", dpi=300)


plt.show()
