#!/bin/bash

/sbin/iptables -t nat -A POSTROUTING -o eno1 -j MASQUERADE
/sbin/iptables -A FORWARD -i eno1 -o br1 -m state --state RELATED,ESTABLISHED -j ACCEPT
/sbin/iptables -A FORWARD -i br1 -o eno1 -j ACCEPT
sudo sysctl -w net.ipv4.ip_forward=1
