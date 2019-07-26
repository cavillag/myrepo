
### Target is Cisco NCS 5508 router. XR OS.

from netmiko import ConnectHandler
from ncclient import manager
from lxml import etree
import json
import time
import os

processing_message="Processing RPC..."
precheck_cmds=('prechecks.txt')
devices_cmds=('devices.txt')
precheck_file=os.path.isfile(precheck_cmds)
devices_file=os.path.isfile(devices_cmds)
cmd_dict={}
pos=0

XML_filter='''
    <hostname xmlns="http://www.cisco.com/ns/yang/Cisco-IOS-XR-sysadmin-nto-misc-set-hostname">
        <name></name>
    </hostname>
'''

def precheck_get(precheck_cmds):
    with open(precheck_cmds) as cmds:
        cmd_list=cmds.readlines()
    return(cmd_list)


def devices_get(devices_cmds):
    with open(devices_cmds) as devs:
        devs_list=devs.readlines()
    return(devs_list)

### Main

while precheck_file is False:
    with open('prechecks.txt','w+') as f:
        precmd_str=f.read()

while devices_file is False:
    with open('devices.txt','w+') as f:
        devs_str=f.read()

cmd_list=precheck_get(precheck_cmds)
devs_list=devices_get(devices_cmds)


### Removing Trailing Spaces

for i in cmd_list:
    cmd_dict[cmd_list[pos]]=i.rstrip()
    pos+=1

pos=0

for i in devs_list:
    devs_list[pos]=i.rstrip()
    pos+=1

print(processing_message)

### Connecting to network devices, retrieving devices hostname

for i in devs_list:
    netconf_session=manager.connect(host=i,port="830",username="admin",password="cisco",hostkey_verify=False,device_params={},allow_agent=False,look_for_keys=False)
    output=netconf_session.get(("subtree", XML_filter))
    hostname=output.data.find('.//{http://www.cisco.com/ns/yang/Cisco-IOS-XR-sysadmin-nto-misc-set-hostname}name')

### subtree string as argument for the manager object means that it will accept an XML string


    session=ConnectHandler(host=i,username="admin",password="cisco",device_type='cisco_ios')

    ### Collecting commands and writing to file with the command name AND hostname of the device

    for key,val in cmd_dict.items():
        sent_cmd=session.send_command_expect(val)
        with open(key+"_"+hostname.text,"w+") as f:
             cmd_output=f.writelines(sent_cmd)

