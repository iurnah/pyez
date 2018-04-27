# Typing-less Junos operation and configuration

To use the scripts you should have SSH access to the Junos device.
Typically, the setup involving the following commands.
1. SSH key generation
    ```
    ssh-keygen
    ```
then move the generated public key to the device as a disk file.

2. SSH pub key configure in the device

    ```
    set system root-authentication load-key-file /etc/ssh/id_rsa.pub
    ```

3. Device nssconf setup
    ```
    set system services netconf ssh
    ```

__getdevFact.py__

First script you may want to test your ssh connection. 

Simply connect the device and return the device fact as json object dump.

__getcfgAll.py__

As a configure backup tool. Return all the configurations of the given device.
Store the returned configuration in folder `cfg` for different format such as:

```
./cfg/all.set
./cfg/all.conf
./cfg/all.xml
./cfg/all.json
```

__getcfgPart.py__

Similar as `getcfgAll.py`, but allow you to specify the "filter" so that a
subset of the device configuration is returned.

__putcfgAll.py__
__putcfgPart.py__
__putcfg.py__

usage: python putcfg.py PATH_TO_THE_CONF_FILE

it takes one argument: the path to a file containing the configuration
to be commited.

allow you upload the
