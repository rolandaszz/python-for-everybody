'''
assignment 3.1
'''
HRS = input('Enter hours: ')
RT = input('Enter rate: ')

try:
    HRS = float(HRS)
    RT = float(RT)
except:
    print('Invalid number')

if HRS < 0 or RT < 0:
    print('Number has to be greater than zero')
    quit()

if HRS > 40:
    OT = RT * 1.5
    OTH = HRS - 40

TPAY = (HRS-OTH) * RT + OTH * OT

print(TPAY)
