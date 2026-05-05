"""def even_odd(num):
    if num%2==0:
        return"even"
    else:
        return"odd"

result=even_odd(50)
print(result)"""
def multiple(num1,num2):
    result=num1*num2
    return result

val_1=int(input("enter a number:"))
val_2=(int(input("enter a number:")))

val=multiple(val_1,val_2)
print(val)
def arithmatic(num1,num2):
    add=num1+num2
    mul=num1*num2
    div=num1/num2
    mod=num1%num2
    sub=num1-num2
    return add,mul,div,mod,sub

val_1=int(input("enter a number:"))
val_2=(int(input("enter a number:")))
res1,res2,res3,res4,res5=arithmatic(val_1,val_2)
val=arithmatic(val_1,val_2)
print(f"product of {val_1} and {val_2} is {res2} ")
print(f"sum of {val_1} and {val_2} is {res1} ")
print(f"division of {val_1} and {val_2} is {res3} ")
print(f"modulo of {val_1} and {val_2} is {res4}")
print(f"subtraction of {val_1} and {val_2} is {res5}")
