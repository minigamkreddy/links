DHCPv6 Server Setup

raju.konduru@globaledgesoft.com
Requirements

    Ubuntu Machine with two ethernet interfaces
    1 Gigabit Switch

Configuration
Install required packages
Install isc-dhcp-server

    sudo apt-get install isc-dhcp-server

Install radvd

    sudo apt-get install radvd

Configure Ethrenet interfaces
Configure WAN interface (eth0)

    IPv4 - DHCP
    IPv6
        Address - 2404:a800:3001:14:   (Ask Ramesh/Raju to get free IPv6 address for using)
        Prefix - 64
        Gateway - 2404:a800:3001:14::1
        DNS Server - 2001:4860:4860::8888 and 2001:4860:4860::8844

Configure LAN interface (eth1)

    IPv4
        Address - 192.168.10.1
        Netmask - 24
        Gateway - Leave empty
        DNS Server - 8.8.8.8
    IPv6
        Address - 6667:c0de:7e57:2a3:15:a:900d:cafe
        Netmask - 64
        Gateway - Leave empty
        Netmask - 2001:4860:4860::8888 and 2001:4860:4860::8844

Enable IP forwarding

    sudo sysctl net.ipv4.ip_forward=1
    sudo sysctl -w net.ipv6.conf.all.forwarding=1

Alternatively to make this configuration permanent enable these two flags in /etc/sysctl.conf
Configure and Run RADVD

    Create /etc/radvd.conf with below configuration

interface eth1

{

AdvSendAdvert on;

AdvManagedFlag on;

AdvOtherConfigFlag on;

AdvCurHopLimit 0;

 

MaxRtrAdvInterval 4;

MinRtrAdvInterval 3;

 

# AdvIntervalOpt on;

AdvDefaultLifetime 1800; # s

AdvReachableTime 36000; # ms

AdvRetransTimer 1000; # ms

 

AdvSourceLLAddress off;

 

prefix 6667:c0de:7e57:2a1::/64

{

AdvOnLink off;

AdvAutonomous off;

AdvValidLifetime 604800;

AdvPreferredLifetime 302400;

};

 

prefix 6667:c0de:7e57:2a2::/64

{

AdvOnLink off;

AdvAutonomous off;

AdvValidLifetime 604800;

AdvPreferredLifetime 302400;

};

 

prefix 6667:c0de:7e57:2a3::/64

{

AdvOnLink off;

AdvAutonomous off;

AdvValidLifetime 604800;

AdvPreferredLifetime 302400;

};

 

prefix 6667:c0de:7e57:2a4::/64

{

AdvOnLink off;

AdvAutonomous off;

AdvValidLifetime 604800;

AdvPreferredLifetime 302400;

};

};

 

    sudo service radvd restart

Configure and Run DHCPD
Configure and Run DHCPv4

    Create /etc/dhcp/dhcpd.conf with below configuration

default-lease-time 600;

max-lease-time 7200;

option subnet-mask 255.255.255.0;

option broadcast-address 192.168.10.255;

option routers 192.168.10.1;

option domain-name-servers 8.8.8.8, 8.8.4.4;

option domain-search "example.com";

 

subnet 192.168.10.0 netmask 255.255.255.0 {

range 192.168.10.10 192.168.10.150;

}

    sudo service isc-dhcp-server

Configure and Run DHCPv6

    Creeate /etc/dhcp/dhcpd6.conf with below configuration

preferred-lifetime 3600;

default-lease-time 3600;

max-lease-time 7200;

log-facility local7;

 

subnet6 6667:c0de:7e57:2a3::/64 {

# Range for clients

range6 6667:c0de:7e57:2a3::4 6667:c0de:7e57:2a3::254;

#

# # Range for clients requesting a temporary address

range6 6667:c0de:7e57:2a3::/64 temporary;

#

# # Additional options

option dhcp6.name-servers 2001:4860:4860::8888,2001:4860:4860::8844;

#

# # UNUSED

# # option dhcp6.domain-search "domain.example";

#

# # Prefix range for delegation to sub-routers

prefix6 6667:c0de:7e58:: 6667:c0de:7e88:: /60;

 

option dhcp-renewal-time 1800;

option dhcp-rebinding-time 2880;

 

option dhcp6.reconf-accept;

 

# # This configuration doesn't still handle the PD request. Refer to

# # the packet capture of the comcast on PD request and match it up.

option fqdn.server-update off;

}

    sudo touch /var/lib/dhcp/dhcpd6.leases
    dhcpd -6 -f -cf /etc/dhcp/dhcpd6.conf -lf /var/lib/dhcp/dhcpd6.leases

Enable IPv4 NATing

    sudo iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -o eth0 -j MASQUERADE
    sudo iptables -t nat -A POSTROUTING -s 192.168.10.0/24 -j SNAT --to-source <WAN(eth0) IP Address>

Enable IPv6 NATing

    sudo ip6tables -t nat -A POSTROUTING -o eth0 -s 6667:c0de:7e57:2a3::/64 -j MASQUERADE
    sudo ip6tables -t nat -A POSTROUTING -o eth0 -s <BR-LAN IP of Gale>/60 -j MASQUERADE

Add IPv6 route

    sudo ip -6 route add <BR-LAN IP of Gale>/60 via <WAN IP of Gale> dev eth1

Verification

    Ping google.com from Gale and Stations
        ping6 google
    Access ipv6-test.com and test-ipv6.com from stations
