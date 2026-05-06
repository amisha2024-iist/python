#in python we can pass a function as argument of another funtion.
def add_1(number):
    return number+1

def square(number):
    return number**2
num=int(input("enter a number"))
res=square(add_1(num))
print(f"result is {res}")
