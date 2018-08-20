'''xml parse'''
import urllib.request as ur
import xml.etree.ElementTree as et

#link to parse
link = 'http://py4e-data.dr-chuck.net/comments_112910.xml'

#link handle
print('Retrieving', link)
lh = ur.urlopen(link)
#link data
ld = lh.read()
print('Retrieved', len(ld), 'characters')

#xml data
xd = et.fromstring(ld)
counts = xd.findall('.//count')

total = 0
idx = 0

for c in counts:
    total += int(c.text)
    idx += 1

print('Tag count', idx)
print('Sum', total)
