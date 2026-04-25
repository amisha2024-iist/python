"""
>=90,grade A
80 and 89,grade B
70 and 79,grade C
60 and 69,grade D
<60,grade F
"""
#if-elif-else
marks = float(input("enter the marks: "))
if marks>=90:
    print("grade is A")
elif marks>=80 and marks<90:
    print("grade is B")
elif marks >= 70 and marks <80:
    print("grade is C")
elif marks >= 60 and marks <70:
    print("grade is D")
elif marks<60:
    print("marks is f")
