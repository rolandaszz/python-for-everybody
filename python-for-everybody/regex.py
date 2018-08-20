'''
Regular Expressions
'''
import re

fh = open('regex_sum_112906.txt', 'r')

num = list()
apl = list()

for fl in fh:
    sfl = fl.rstrip()
    apl = re.findall('[0-9]+', sfl)
    if apl:
        num.append(apl)

total = 0

for nv in num:
    for n in nv:
        total += int(n)

print(total)

#Python 3:
#import re
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
