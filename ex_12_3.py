# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ') #'http://py4e-data.dr-chuck.net/known_by_Abid.html'
count = int(input('Enter count: '))
position = int(input('Enter position: '))
position2 = position

while count != 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        position2 = position2 - 1
        if position2 == 0:
            url = tag.get('href', None)
            print(url)
    position2 = position
    count = count - 1
answer = url.split('_')
answer = answer[2].split('.')
answer = answer[0]
print('The answer to the assignment for this execution is"'+answer+'".')
