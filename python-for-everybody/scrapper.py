'''scrapper'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

cnturl = "http://py4e-data.dr-chuck.net/comments_112908.html"

html = urlopen(cnturl).read()
clean = BeautifulSoup(html, 'html.parser')

sp = clean('span')

tsum = 0

for numl in sp:
    tsum += int(numl.contents[0])

print(tsum)
