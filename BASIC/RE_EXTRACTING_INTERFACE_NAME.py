import re

with open("resfile.txt") as f:
    hachiko=f.readlines()

interfacenames=[]

for i in hachiko:
    match_re=re.search(r'(TenGigE./././..?/.)(.+)',i)
    if match_re:
        if match_re.group(1) not in interfacenames:
            interfacenames.append(match_re.group(1))

for i in interfacenames:
    print("default interface "+ i + "\n!")
