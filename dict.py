'''9.4 Write a program to read through the mbox-short.txt and figure
out who has the sent the greatest number of mail messages. The program looks
for 'From ' lines and takes the second word of those lines as the person
who sent the mail. The program creates a Python dictionary that maps the
sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using
a maximum loop to find the most prolific committer.'''

fh = open('mbox-short.txt','r')
wc = dict()

for fl in fh:
    sl = fl.split()
    for sw in sl:
        if sw == 'From':
            wc[sl[1]] = wc.get(sl[1], 0)+1

sender = None
emailcount = None

for e, c in wc.items():
    if emailcount is None or c > emailcount:
        sender = e
        emailcount = c

print(sender, emailcount)
