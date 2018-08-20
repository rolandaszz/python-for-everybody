'''json parse'''
import urllib.request as ur
import json

#link to parse
link = 'http://py4e-data.dr-chuck.net/comments_112911.json'

#link handle
print('Retrieving', link)
lh = ur.urlopen(link)
#link data
ld = lh.read().decode()
print('Retrieved', len(ld), 'characters')

#parse
try:
    jdata = json.loads(ld)
except:
    jdata = None

total = 0
idx = 0

for cmn in jdata['comments']:
    total += int(cmn['count'])
    idx += 1

print('Tag count', idx)
print('Sum', total)
