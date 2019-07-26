import re
import os

file="show version_ATT-LAB-L-CON-NCS5502-1"
list=[]
output=''

with open(file) as f:
    cmd_string=f.readlines()

for i in cmd_string:
    matchobj=re.sub(r'<dev>','cavillag',i)
    list.append(matchobj)
for i in list:
    matchobj=re.sub(r'<version>','6.5.3',i)
    output=output+"\n"+matchobj

print(output)
