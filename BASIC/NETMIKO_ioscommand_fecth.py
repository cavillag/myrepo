
### Target is Cisco NCS 5508 router. XR OS.

from netmiko import ConnectHandler
import json
import time
import os

processing_message="Processing RPC..."
precheck_cmds=('prechecks.txt')
precheck_file=os.path.isfile(precheck_cmds)
cmd_dict={}
pos=0

def precheck_get(precheck_cmds):
    with open('prechecks.txt') as cmds:
        cmd_list=cmds.readlines()
    return(cmd_list)

### Main

while precheck_file is False:
    with open('prechecks.txt','w+') as f:
        precmd_str=f.read()


cmd_list=precheck_get(precheck_cmds)

### Removing Trailing Spaces

for i in cmd_list:
    cmd_dict[cmd_list[pos]]=i.rstrip()
    pos+=1

print(processing_message)

### Connecting to network device

session=ConnectHandler(host="10.88.242.37",username="admin",password="cisco",device_type='cisco_ios')

### Collecting commands and writing to file with the command name

for key,val in cmd_dict.items():
    output=session.send_command_expect(val)
    with open(key,"w+") as f:
        cmd_output=f.writelines(output)

