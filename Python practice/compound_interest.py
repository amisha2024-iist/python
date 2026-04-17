"""
amount=p(1+(r/100))**t
ci=amount-p
"""
principal=float(input("enter principal amount:"))
rate=float(input("enter rate of interest:"))
time=float(input("Enter the time duration: "))
amount1=principal*(1+rate/100)**time
amount2=principal*pow((1+rate/100),time)
print(amount1,amount2)