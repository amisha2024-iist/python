"""def add(a,b):
    return a+b
#positional argument-passing the argument in order of their position.
result=add(10,20)"""

#default argument-if we given a default valur to an argument then it will take that value as default even if we don't given the value of it
def add(a,b=10):
    return a+b
result=add(10,40)
print(result)
