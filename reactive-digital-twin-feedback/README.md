# Reactive Digital Twin Feedback


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

