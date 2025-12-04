#!/usr/bin/env python

import os

from mininet.log import setLogLevel, info
from mininet.term import makeTerm
from mn_wifi.sixLoWPAN.link import LoWPAN
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()
    path = os.path.dirname(os.path.abspath(__file__))

    info("*** Creating nodes\n")
    sensor1 = net.addSensor('sensor1', ip6='fe80::1/64', panid='0xbeef',
                            dodag_root=True, storing_mode=2)
    sensor2 = net.addSensor('sensor2', ip6='fe80::2/64', panid='0xbeef',
                            storing_mode=2)
    sensor3 = net.addSensor('sensor3', ip6='fe80::3/64', panid='0xbeef',
                            storing_mode=2)
    sensor4 = net.addSensor('sensor4', ip6='fe80::4/64', panid='0xbeef',
                            storing_mode=2)
    sensor10 = net.addSensor('sensor10', ip6='fe80::10/64', panid='0xbeef',
                             dodag_root=True, dodagid='fd1c:be8a:173f:8e80::1',
                             storing_mode=2, phy='wpan0', inNamespace=False)

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Adding links\n")
    net.addLink(sensor1, sensor2, cls=LoWPAN)
    net.addLink(sensor1, sensor3, cls=LoWPAN)
    net.addLink(sensor3, sensor4, cls=LoWPAN)

    info("*** Starting network\n")
    net.build()

    # You must have the nonstoring_mode branch from https://github.com/linux-wpan/rpld
    info("*** Configuring RPLD\n")
    net.configRPLD(net.sensors)

    makeTerm(sensor10, title='phy', cmd="bash -c 'python {}/receiver.py;'".format(path))
    makeTerm(sensor1, title='gateway', cmd="bash -c 'python {}/gateway.py;'".format(path))
    makeTerm(sensor1, title='tcpdump-virtual', cmd="bash -c 'tcpdump -i sensor1-pan0 -w {}/sensor1.pcap;'".format(path))
    makeTerm(sensor10, title='tcpdump-phy', cmd="bash -c 'tcpdump -i lowpan0 -w {}/phy.pcap;'".format(path))

    info("*** Running CLI\n")
    CLI(net)

    info('*** Kill xterm terminals\n')
    os.system('pkill -9 -f \"xterm\"')

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
