#!/usr/bin/env python3
import random
import socket
import sys
from time import sleep
from scapy.all import IP, UDP, TCP, Ether, get_if_hwaddr, get_if_list, sendp

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

def main():
    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()
    pkt = Ether(src=get_if_hwaddr(iface)) / IP(dst=addr, tos=1) / 
        TCP(sport=1234, dport=4321, flags="S") / sys.argv[2]
    pkt.show2()
    #hexdump(pkt)
    try:
        for i in range(int(sys.argv[3])):
            sendp(pkt, iface=iface)
            pkt.show2()
            sleep(1)
    except KeyboardInterrupt:
        raise

if __name__ == '__main__':
    main()
