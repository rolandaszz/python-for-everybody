'''integers only'''

small = None
large = None

while True:
    num = input('Please enter a numner: ')
    try:
        num = int(num)
    except:
        if num == 'done':
            break
        else:
            print('Invalid input')
            continue
    if small is None and large is None:
        small = num
        large = num
    if small > num:
        small = num
    if large < num:
        large = num
print('Maximum is', large)
print('Minimum is', small)
