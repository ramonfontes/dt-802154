#!/usr/bin/env python

import os

from mininet.log import setLogLevel, info
from mininet.term import makeTerm
from mn_wifi.sixLoWPAN.link import LoWPAN
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

"""This example creates a simple network topology with 4 nodes

       sensor1 (root)
      /       \
    /          \
sensor2      sensor3
               |
               |
             sensor4

Note: To establish MQTT communication over IPv6, you must ensure 
that your broker is configured to support it. For example, if 
you're using Mosquitto, add the following line to your mosquitto.conf file:

listener 1883 ::

This allows Mosquitto to listen on all available IPv6 interfaces.

Then, you can use the mosquitto_pub and mosquitto_sub commands like this:

sensor2$ mosquitto_pub -h fe80::1%sensor2-pan0 -t topic -m message
sensor3$ mosquitto_sub -h fe80::1%sensor3-pan0 -t topic
"""


def topology():
    "Create a network."
    net = Mininet_wifi()
    path = os.path.dirname(os.path.abspath(__file__))

    info("*** Creating nodes\n")
    # There is no need to set the node position.
    # Signal range and position won't work as we expect
    # because there is no wmediumd-like code for mac802154_hwim yet.
    # However, you may want to add mobility and node position
    # and use wpan-hwsim for some purposes.
    # dodag_root and storing mode only work with RPLD
    # supported storing modes:
    # **** RPL_DIO_NO_DOWNWARD_ROUTES_MAINT = 0
    # **** RPL_DIO_NONSTORING = 1
    # **** RPL_DIO_STORING_NO_MULTICAST = 2
    # **** RPL_DIO_STORING_MULTICAST = 3
    sensor1 = net.addSensor('sensor1', ip6='fe80::1/64', panid='0xbeef',
                            dodag_root=True, storing_mode=2)
    sensor2 = net.addSensor('sensor2', ip6='fe80::2/64', panid='0xbeef',
                            storing_mode=2)
    sensor3 = net.addSensor('sensor3', ip6='fe80::3/64', panid='0xbeef',
                            storing_mode=2)
    sensor4 = net.addSensor('sensor4', ip6='fe80::4/64', panid='0xbeef',
                            storing_mode=1)
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
