"""
when all the length of the sides of the triangle is known
semi perimeter(s)=(a+b+c)/2
area=square root of (s*(s-a)*(s-b)*(s-c))
"""
a=float(input("enter the length of the sides of the triangle"))
b=float(input("enter the length of the sides of the triangle"))
c=float(input("enter the length of the sides of the triangle"))
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)**0.5
print("the area of the triangle is:",area)