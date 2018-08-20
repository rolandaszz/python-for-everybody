def computepay(hrs, pay):
    if hrs <= 40:
        return hrs * pay
    else:
        return ((hrs-40) * pay * 1.5) + 40 * pay

HRS = input('Enter Hours: ')
PAY = input('Enter Pay: ')

HRS = float(HRS)
PAY = float(PAY)

print(computepay(HRS, PAY))
