#!/usr/bin/evn python

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

pkg = 'junos-install-mx-x86-64-17.2R1.13.tgz'

with Device(host='router1.example.net') as dev:
    sw = SW(dev)
    ok = sw.install(package=pkg, validate=True) 
    if ok:
        sw.reboot()
