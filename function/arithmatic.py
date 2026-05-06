"""
a simple arithmatic module
"""
def add(num1,num2):
    return num1+num2

def square_root(number):
    return number**0.5

#--name--variable
print(f"__name__ value in arithmatic.py =>{__name__}")
if __name__ == "__main__":
    a = 10
    b = 30
    result=add(a,b)
    print(result)
