import urllib.request,urllib.parse,urllib.error
import json
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter url-')
data = urllib.request.urlopen(url).read()

info = json.loads(data)
print('User count:', len(info))
sum=0
for item in info['comments']:
    sum=sum+int(item['count'])
print(sum)
