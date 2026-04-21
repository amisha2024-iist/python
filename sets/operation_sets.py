student1={"english","math","cs","os"}
student2={"english","biology","chemistry","physics"}
student3={"english","physics","dsa"}
print(student1,type(student1))
print(student2,type(student2))
#comman subject of student1 and student2
common_subject = student1.intersection(student2)
print(common_subject)
#all subject of s1 ands2=union
all_subjects=student1.union(student2)
print(all_subjects)
call_student=student1|student2|student3
print(call_student)

#difference of sets
days={"mon","tue","wed","thu","fri","sat","sun"}
weekends={"sat","sun"}
#weekdays=days-weekends #element of days which are Not in weekends
weekdays=days.difference(weekends)
