"""from operator import index

concatenation,repetition,membership,
count,index
min,max,sum"""

student_detail1 = (1001,"john")
student_detail2 = (78.5,91.0,83.5,79.5)

# +
student_details = student_detail1 + student_detail2
print(student_details)

#*(repetition)
t1 = ("class 12",5000)
print(t1*3)

#membership operation
#in,not in
print(91.0 in student_details)
print(99.0 not in student_details)

#count
t2=(10,4,1,9,3,0)
#tuple.count(element)
print(t2.count(1))

#index()
#tuple.index(element)
print(t2.index(3))
print(t1.index(5000))
#min
t3=(10,4,6,3,7,0,4,7)
#min(tuple)
#max(tuple)
#sum(tuple)
print(f"smallest number: {min(t3)}") #0
print(f"largest number: {max(t3)}")#10
print(f"sum: {sum(t3)}")#41

