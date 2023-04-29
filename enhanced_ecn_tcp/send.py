#!/usr/bin/env python3
print("Here1")
import random
print("Here2")
import socket
print("Here3")
import sys
print("Here4")
from time import sleep
print("Here5")
from scapy.all import IP, UDP, TCP, Ether, get_if_hwaddr, get_if_list, sendp
print("Here6")

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def main():

    # if len(sys.argv)<4:
    #     print('pass 2 arguments: <destination> "<message>" <duration>')
    #     exit(1)

    avgrtt = 0


    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()

    pkt = Ether(src=get_if_hwaddr(iface)) / IP(dst=addr, tos=1) / TCP(sport=1234, dport=4321, flags="S") / sys.argv[2]
    pkt.show2()
    #hexdump(pkt)
    try:
      for i in range(int(sys.argv[3])):
        print("Here")
        sendp(pkt, iface=iface)
        pkt.show2()
        # a=sr1(pkt)
        # print(a.time- pkt.sent_time)
        # avgrtt+=(a.time - pkt.sent_time)
        sleep(1)
        # print("Average RTT = ",avgrtt/sys.argv[3])
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    print("Here7")
    main()
