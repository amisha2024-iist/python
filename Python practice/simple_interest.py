"""
simple interest=(p*r*t)/100
p=principal amount
r=rate of interest
t=time duration
"""
principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time duration: "))
si=(principal*time*rate)/100
print("The interest is",si)
