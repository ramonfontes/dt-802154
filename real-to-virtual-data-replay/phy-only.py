#!/usr/bin/env python

import os
import sys

from mininet.log import setLogLevel, info
from mininet.term import makeTerm
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()
    path = os.path.dirname(os.path.abspath(__file__))
    ip6 = sys.argv[1]
    node_id = sys.argv[2]

    info("*** Creating nodes\n")
    sensor1 = net.addSensor('sensor1', ip6=ip6, panid='0xbeef', dodag_root=False,
                            storing_mode=2, phy='wpan0', inNamespace=False)

    info("*** Configuring nodes\n")
    net.configureNodes()

    info("*** Starting network\n")
    net.build()

    # You must have the nonstoring_mode branch from https://github.com/linux-wpan/rpld
    info("*** Configuring RPLD\n")
    net.configRPLD(net.sensors)

    makeTerm(sensor1, title='sensor1', cmd="bash -c 'python {}/send.py;'".format(path))

    info("*** Running CLI\n")
    CLI(net)

    info('*** Kill xterm terminals\n')
    os.system('pkill -9 -f \"xterm\"')

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()