#!/usr/bin/env python3
import sys
import os
from scapy.all import (FieldLenField, FieldListField, IntField, IPOption, ShortField, get_if_list, sniff)
from scapy.layers.inet import _IPOption_HDR


def get_if():
    ifs = get_if_list()
    iface = None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def handle_pkt(pkt):
    print("got a packet")
    pkt.show2()
#    hexdump(pkt)
    sys.stdout.flush()

def main():
    ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth' in i]
    iface = ifaces[0]
    print("sniffing on %s" % iface)
    sys.stdout.flush()
    sniff(filter="tcp", iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
