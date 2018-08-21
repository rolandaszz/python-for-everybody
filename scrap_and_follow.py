'''scrap and follow'''
from urllib import request
from re import findall
from bs4 import BeautifulSoup

#initial url
iurl = ' http://py4e-data.dr-chuck.net/known_by_Laurie.html'

#position and depth -1
initial_pos = 17
depth = 6


def getlink(url, pos):
    '''open and parse'''
    getlinkidx = 0
    html = request.urlopen(url).read()
    soap = BeautifulSoup(html, 'html.parser')
    tags = soap('a')
    for tag in tags:
        if getlinkidx == pos:
            link = tag.get('href', None)
            print('Following: ', link)
        getlinkidx += 1
    return link


idx = 0
#initial link
print('Initial url:', iurl)

if idx == 0:
    print('Iteration:', idx)
    linktofollow = getlink(iurl, initial_pos)
    print('Name:', findall(r'known_by_(.+)\.', linktofollow))
    idx += 1

while depth >= idx:
    print('Iteration:', idx)
    linktofollow = getlink(linktofollow, initial_pos)
    name = findall(r'known_by_(.+)\.', linktofollow)
    print('Name:', name)
    idx += 1

print('Result:', name)
