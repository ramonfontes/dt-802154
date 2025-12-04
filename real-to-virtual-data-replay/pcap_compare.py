#!/usr/bin/env python3
from scapy.all import rdpcap, UDP, Raw
import sys
import hashlib

# ---------------------------------------------------------
# Extract the UDP payloads (Raw data only) from a PCAP file
# ---------------------------------------------------------
def extract_udp_payloads(pcap_file):
    packets = rdpcap(pcap_file)
    payloads = []

    for pkt in packets:
        if UDP in pkt and Raw in pkt:
            payloads.append(bytes(pkt[Raw].load))

    return payloads

# ---------------------------------------------------------
# Compute SHA-256 hash of the payload for comparison
# ---------------------------------------------------------
def hash_payload(payload):
    return hashlib.sha256(payload).hexdigest()

# ---------------------------------------------------------
# Optional: Calculate byte-level similarity percentage
# (Uses Levenshtein distance — disabled by default)
# ---------------------------------------------------------
def similarity_bytes(a, b):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio() * 100

# ---------------------------------------------------------
# Compute Jaccard similarity:
# (Intersection / Union) * 100
# Good for comparing sets of payloads
# ---------------------------------------------------------
def jaccard_similarity(set1, set2):
    inter = len(set1 & set2)
    union = len(set1 | set2)
    if union == 0:
        return 0.0
    return (inter / union) * 100.0

# ---------------------------------------------------------
# Main comparison logic
# ---------------------------------------------------------
def main(p1, p2):
    data1 = extract_udp_payloads(p1)
    data2 = extract_udp_payloads(p2)

    print(f"[INFO] UDP packets with payload in {p1}: {len(data1)}")
    print(f"[INFO] UDP packets with payload in {p2}: {len(data2)}\n")

    # Hash maps: hash -> payload
    hashes1 = {hash_payload(p): p for p in data1}
    hashes2 = {hash_payload(p): p for p in data2}

    set1 = set(hashes1.keys())
    set2 = set(hashes2.keys())

    # Identify equal and unique payloads
    iguais = set1 & set2
    exclusivos1 = set1 - set2
    exclusivos2 = set2 - set1

    # -----------------------------------------------------
    # Compute similarity metrics
    # -----------------------------------------------------
    jac = jaccard_similarity(set1, set2)

    tamanho_similar = 0
    total_min = min(len(data1), len(data2))

    for i in range(total_min):
        if len(data1[i]) == len(data2[i]):
            tamanho_similar += 1

    tamanho_pct = (tamanho_similar / total_min) * 100 if total_min > 0 else 0

    print("======== SIMILARITY METRICS ========")
    print(f"Jaccard similarity:       {jac:.2f}%")
    print(f"Same-size payload ratio:  {tamanho_pct:.2f}%")
    print(f"Identical payloads:       {len(iguais)}")
    print(f"Unique in PCAP 1:         {len(exclusivos1)}")
    print(f"Unique in PCAP 2:         {len(exclusivos2)}")

    print("\n======== IDENTICAL UDP DATA ========")
    for h in iguais:
        print(f"  HASH: {h}   SIZE: {len(hashes1[h])} bytes")

    print("\n======== UNIQUE UDP DATA IN PCAP 1 ========")
    for h in exclusivos1:
        print(f"  HASH: {h}   SIZE: {len(hashes1[h])} bytes")

    print("\n======== UNIQUE UDP DATA IN PCAP 2 ========")
    for h in exclusivos2:
        print(f"  HASH: {h}   SIZE: {len(hashes2[h])} bytes")

    print("\n[OK] UDP-only data comparison finished.")

# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 pcap_udp_data_diff.py file1.pcap file2.pcap")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])