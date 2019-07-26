import re
import os

file="show version_ATT-LAB-L-CON-NCS5502-1"

with open(file) as f:
    cmd_string=f.readlines()

for i in cmd_string:
    matchobj=re.search(r'uptime is (\d+) days (\d+) hours (\d+) minutes',i)
    if matchobj:
        days_uptime=matchobj.group(1)

for i in cmd_string:
    matchobj=re.search(r'Version      : (\d.\d.\d)',i)
    if matchobj:
        router_version=matchobj.group(1)

print("System has been up for: "+days_uptime+" days and it is running release code: "+router_version)
