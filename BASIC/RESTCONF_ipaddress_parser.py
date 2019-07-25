import json
from lxml import etree
import requests
from requests.auth import HTTPBasicAuth



auth = HTTPBasicAuth('admin', 'C1sco12345')
headers = {
     'Content-Type': 'application/yang.data+xml'
}

url = 'https://198.18.134.11:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1/ip/address/primary'
response = requests.get(url, headers=headers, auth=auth, verify=False)

# print(response.text)

xml_obj=etree.fromstring(response.text)
print(xml_obj)
print(type(xml_obj))

### etree fromstring method passes a string to the etree function and the said string gets converted to an lxml object.
### <class 'lxml.etree._Element'>

ip_address_gig1=xml_obj.find('.//{http://cisco.com/ns/yang/Cisco-IOS-XE-native}address')

print(ip_address_gig1.text)

### Based on the configuration fromatted as XML we can parse certain files via XML tag and find function of lxml objects.
