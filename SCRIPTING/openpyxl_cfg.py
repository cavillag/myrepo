import openpyxl

wb=openpyxl.load_workbook("GUARNC160.xlsx")
print(wb.sheetnames)
sheet=wb["IP Assignment"]

#print(sheet["A1"].value)

for i in range(2,34,2):
    interface=sheet["W"+str(i)].value
    vlan=sheet["T"+str(i)].value
    ipaddress=sheet["S"+str(i)].value
    mask=sheet["N"+str(i)].value
    vrf=sheet["P"+str(i)].value
    print('''
        interface Hundred{0}.{1}
        encapsulation dot1q {1}
        rewrite ingress tag pop 1 symmetric
        !
        interface BVI {1}
        vrf {4}
        ipv4 address {2} {3}
        mac-address {1}.0000.0000.0000
        !
        l2vpn
            bridge-group BD{1}
            bridge-domain BD{1}
            interface Hundred{0}.{1}
            routed interface BVI {1}
            !
            !'''.format(interface,vlan,ipaddress,mask,vrf))

