import re


t = 'http://py4e-data.dr-chuck.net/known_by_Anayah.html'


p = re.findall('known_by_(.+)\.', t)

print(p)
