#!/usr/bin/evn python

import sys
import json
from lxml import etree

from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

hostname = ""
username = "root"
password = ""
key_path = "./id_rsa"

conf_filter = "all"
file_path = './cfg/' + conf_filter.replace('/', '-')
out_suffix = ['', 'set', 'text', 'json']

try:
    with Device(host=hostname, user=username, ssh_private_key_file=key_path) as dev:
        for suffix in out_suffix:
            suffix = 'xml' if not suffix else suffix
            data = dev.rpc.get_config(options={'format':suffix})
            if suffix == 'json':
                config = json.dumps(data, indent=2)
            else:
                config=etree.tostring(data, encoding='unicode')   
            #print(config)
            file_name = file_path + '.' + suffix
            with open(file_name, "w") as text_file:
                text_file.write(config)

            print ("Wrote total {0} bytes to file: {1}".format(sys.getsizeof(config), file_name))
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)
except Exception as err:
    print (err)
    sys.exit(1)
