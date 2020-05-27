import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

sum=0
while True:
    url=input("Enter -")
    if len(url)<1:break
    xml=urllib.request.urlopen(url,context=ctx).read()
    tree=ET.fromstring(xml)
    for count in tree.findall('comments/comment/count'):
        sum=sum+int(count.text)
    print(sum)
    break;
