"""
if marks>=60 then student will pass else they will fail
and if the student is pass,then only we print the grade.
>=90,grade A
80 and 89,grade B
70 and 79,grade C
60 and 69,grade D
<60,grade F
"""
marks=float(input("enter your marks; "))

if marks>=60:
    print("congratulations! you have passed the examinations ")
    if marks>=90:
        print("your grade is A")
    elif 80<= marks <=90:
        print("your grade is B")
    elif 70<=marks<=80:
        print("your grade is C")
    else:
        print("your grade is D")
else:
    print("you have failed the exam,study hard next time")
