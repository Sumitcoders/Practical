p = float(input('Enter principal amount: '))
t = float(input('Enter the time (in years): '))
r = float(input('Enter the rate of intrest: '))

si = (p*t*r)/100
print(f"The simple intrest is {si} rupees and the total amount is {si + p} rupees")