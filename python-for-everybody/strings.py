'''
6.5 Write code using find() and string slicing (see section 6.10)
to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475"

#hardcode :(
zpos = text.find('0')
fpos = text.find('5')+1

num = float(text[zpos:fpos])
print(num)
