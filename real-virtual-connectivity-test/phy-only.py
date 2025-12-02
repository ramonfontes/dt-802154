#!/usr/bin/env python

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()

    ip6 = sys.argv[1]

    info("*** Creating node\n")
    net.addSensor('sensor1', ip6=ip6, panid='0xbeef', dodag_root=False,
                  storing_mode=2, phy='wpan0', inNamespace=False)

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Starting network\n")
    net.build()

    # You must have the nonstoring_mode branch from https://github.com/linux-wpan/rpld
    info("*** Configuring RPLD\n")
    net.configRPLD(net.sensors)

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
