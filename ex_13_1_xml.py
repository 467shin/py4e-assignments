import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
result = 0

#while True:
address = input('Enter URL: ') #http://py4e-data.dr-chuck.net/comments_1588330.xml
#if len(address) < 1: break

parms = dict()
parms['address'] = address
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

nums = tree.findall('.//count')
for num in nums:
    num = int(num.text)
    result = result + num
    count = count + 1
#break
print('Count:', count)
print('Sum:', result)
