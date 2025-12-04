# Real-to-Virtual Data Replay

This section describes the procedure used to execute the emulated network and replay real sensor data inside the Mininet-WiFi environment. The setup integrates virtual IEEE 802.15.4/6LoWPAN nodes with physical sensor devices, enabling direct comparison between real traffic and its replicated virtual counterpart.

## Running the emulated network

The emulated network is launched on the laptop using Mininet-WiFi extended with 802.15.4 and 6LoWPAN support. A physical sensor node is also attached to the laptop and bridged to the virtual topology.

```
sudo python topo.py
```

## Activating the Physical Device (Computer #1)

Each physical device uses the script `phy-only.py`. The script expects two arguments:

- Argument 1: IPv6 address (including prefix)
- Argument 2: Node ID

```
sudo python phy-only.py fe80::2/64 1
```

## Activating the Physical Device (Computer #2)


```
sudo python phy-only.py fe80::3/64 2
```


## Comparing PCAP Traces

To validate the replay accuracy, the captured physical traffic (phy.pcap) is compared against the virtual network traffic (e.g., sensor1.pcap).

Run the comparison tool:

```
python pcap_compare.py phy.pcap sensor1.pcap

```

This script analyzes only UDP payloads, computes similarity metrics, and identifies matching and non-matching packets between the real and virtual traces.