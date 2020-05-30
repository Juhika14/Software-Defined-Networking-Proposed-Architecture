#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

    c1 = net.addController('c1', controller=RemoteController, ip="54.162.138.146", port=6633)
    c2 = net.addController('c2', controller=RemoteController, ip="35.153.204.187",port=6633)



    h1 = net.addHost( 'h1', ip='192.168.1.10' )
    h2 = net.addHost( 'h2', ip='192.168.1.20' )
    h3 = net.addHost( 'h3', ip='172.168.2.40' )
    h4 = net.addHost( 'h4', ip='172.168.2.50' )

    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3=net.addSwitch( 's3' )
    s4=net.addSwitch( 's4' )
    s5=net.addSwitch( 's5' )

    s1.linkTo( h1 )
    s2.linkTo( h2 )
    s4.linkTo( h3 )
    s5.linkTo( h4 )
    s1.linkTo( s2 )
    s2.linkTo( s3 )
    s3.linkTo( s4 )
    s4.linkTo( s5 )


    net.build()
