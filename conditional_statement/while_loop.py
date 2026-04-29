"""
while condition
    statement1
    statement2
    ...
    statementN
"""
"""for num in range(1,10,2):
     print(num)"""

num=1
while num<6:
    print(num)
    num=num+1 #if we don't do this incrementation then it will go in an infinite loop.
correct_password="Python"
while True:
    password=input("enter your password: ")
    if password == correct_password:
        print("your password is correct!congrats")
        break
    else:
        print("your password is incorrect,try again")

print("logged in!")
num=20
while num>=10:
    print(num)
    num=num-2
