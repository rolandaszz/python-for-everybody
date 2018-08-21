fname = input('Enter file name: ')
fh = open(fname)

for fl in fh:
    fl = fl.rstrip().upper()
    print(fl)
