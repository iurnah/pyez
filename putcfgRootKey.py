from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError

hostname = ""
username = "root"
password = ""
key_path = "./id_rsa"

try:
    with Device(host=hostname, user=username, ssh_private_key_file=key_path) as dev:   
        with Config(dev, mode='private') as cu:  
            cu.load('set root-authentication load-key-file /etc/ssh/id_rsa.pub', format='set')
            cu.pdiff()
            cu.commit()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
    sys.exit(1)
except Exception as err:
    print (err)
    sys.exit(1)
