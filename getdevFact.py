#!/usr/bin/evn python

import sys
import yaml
import json 
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

#hostname = "argon-forge-26.spglab.juniper.net"
hostname = ""
username = "root"
password = ""
key_path = "./id_rsa"

try:
    with Device(host=hostname, user=username, ssh_private_key_file=key_path) as dev:   
        print (json.dumps(dev.facts))
        #yaml.dump(dev.facts, sys.stdout)
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)
except Exception as err:
    print (err)
    sys.exit(1)
