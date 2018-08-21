'''json api call'''
import urllib.request, urllib.parse
import json

drchuckapi = 'http://py4e-data.dr-chuck.net/geojson?'
location = 'Dartmouth'

url = drchuckapi + urllib.parse.urlencode(
    {'address': location}

)

print('Retrieve url', url)
uh = urllib.request.urlopen(url)
ud = uh.read().decode()
print('Retrieved', len(ud), 'characters')

try:
    js = json.loads(ud)
except:
    js = None

locationId = js["results"][0]["place_id"]

print('Place Id', locationId)
