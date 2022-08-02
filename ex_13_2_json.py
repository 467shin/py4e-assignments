import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0

address = input('Enter location: ') #'http://py4e-data.dr-chuck.net/comments_1588331.json'

parms = dict()
parms['address'] = address
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
info = json.loads(data)
info = info['comments']

print('Retrieved', len(data), 'characters')
print('Count:', len(info))

#print(data.decode())

for item in info:
    sum = sum + item['count']
print(sum)
