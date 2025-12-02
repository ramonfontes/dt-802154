# Real-Virtual Connectivity Test

This use case demonstrates that physical IEEE 802.15.4 devices and virtual nodes running inside the emulated environment can communicate reliably as part of a unified hybrid network. The experiment is divided into three stages: (i) running the emulated network, (ii) activating the physical gateway interface, and (iii) testing connectivity across both domains.

## Running the emulated network

The emulated network is launched on the laptop using Mininet-WiFi extended with 802.15.4 and 6LoWPAN support. A physical sensor node is also attached to the laptop and bridged to the virtual topology.

```
$ sudo python topo.py
```

After initialization, we start the physical sensor in lowpan0 interface. The following examples illustrate three nodes with their IPv6 addresses:

Physical sensor attached to the laptop:

```
mininet-wifi> sensor10 ifconfig lowpan0
lowpan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1280
        inet6 fd1c:be8a:173f:8e80::1  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::5  prefixlen 64  scopeid 0x20<link>
        unspec 10-E2-D5-FF-FF-00-04-BB-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 161  bytes 14991 (14.9 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 697  bytes 61680 (61.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Virtual sensor (sensor1):
```
mininet-wifi> sensor1 ifconfig sensor1-pan0
sensor1-pan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1280
        inet6 fd3c:be8a:173f:8e80::1  prefixlen 64  scopeid 0x0<global>
        inet6 fe80::1  prefixlen 64  scopeid 0x20<link>
        unspec 9A-46-05-4D-9D-F4-C2-8C-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 5546  bytes 758228 (758.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2167  bytes 154568 (154.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

Virtual sensor (sensor4):
```
mininet-wifi> sensor4 ifconfig sensor4-pan0
sensor4-pan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1280
        inet6 fe80::4  prefixlen 64  scopeid 0x20<link>
        inet6 fd3c:be8a:173f:8e80:402:135:9dfe:a497  prefixlen 64  scopeid 0x0<global>
        unspec 06-02-01-35-9D-FE-A4-96-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
        RX packets 2847  bytes 352354 (352.3 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2851  bytes 382500 (382.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

These interfaces confirm that 6LoWPAN is operational in the emulated environment, and each node has a globally routable IPv6 address within its assigned prefix.

## Activating the Physical Device (Computer #1)

The physical sensor node connected to the laptop is enabled through a simple forwarding script:

```
$ sudo python phy-only.py
```

This script captures packets from the physical IEEE 802.15.4 interface, injects them into the virtual network, and forwards packets from the emulated topology back to the real device. At this point, the physical and virtual nodes form a single logical network.

## Connectivity Tests Between Physical and Virtual Nodes

Ping from physical → physical

```
mininet-wifi> sensor1 ping -c1 fd1c:be8a:173f:8e80::1
PING fd1c:be8a:173f:8e80::1 (fd1c:be8a:173f:8e80::1) 56 data bytes
64 bytes from fd1c:be8a:173f:8e80::1: icmp_seq=1 ttl=64 time=16.7 ms

--- fd1c:be8a:173f:8e80::1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 16.651/16.651/16.651/0.000 ms
```

Ping from physical → virtual (sensor1)

```
mininet-wifi> sensor1 ping -c1 fd3c:be8a:173f:8e80::1
PING fd3c:be8a:173f:8e80::1 (fd3c:be8a:173f:8e80::1) 56 data bytes
64 bytes from fd3c:be8a:173f:8e80::1: icmp_seq=1 ttl=64 time=17.5 ms

--- fd3c:be8a:173f:8e80::1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 17.502/17.502/17.502/0.000 ms
```
Ping from physical → virtual (sensor4)

```
mininet-wifi> sensor1 ping -c1 fd3c:be8a:173f:8e80:402:135:9dfe:a497
PING fd3c:be8a:173f:8e80:402:135:9dfe:a497 (fd3c:be8a:173f:8e80:402:135:9dfe:a497) 56 data bytes
64 bytes from fd3c:be8a:173f:8e80:402:135:9dfe:a497: icmp_seq=1 ttl=62 time=19.2 ms

--- fd3c:be8a:173f:8e80:402:135:9dfe:a497 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 19.203/19.203/19.203/0.000 ms
```