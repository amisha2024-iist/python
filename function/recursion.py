"""
recursion is a process in which a function call itself till a certain condition is not meet.
factorial of n=n*(n-1)*n-2*(n-3)*........2*1
4!=4*3*2*1=24
"""
#without recursion
"""def fact(num):
    factorial=1
    while num>1:
        factorial*=num
        num-=1
    return factorial
n=5
print(f"factorial of {n} is {fact(n)}")
"""
def fact_rec(num):
    if num==1:
        return 1
    else:
        factorial=num*fact_rec(num-1)
        return factorial

print(fact_rec(6))
