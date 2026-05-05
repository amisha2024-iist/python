#args-variable length positional argument(0-n).
"""def add(*args):
    return sum(args)
result=add(10,30,3,5,6,24,56,54)
print(result)
#args is not mendatory it should be any variable,args is just standard form write this program if we take *num also then the program will run smoothly without giving any kind of error."""

def student_details(sid,sname,*marks):
    if len(marks)==0:
        print(f"{sname} with id{sid} was absent in all exam ")
    else:
        percent=sum(marks)/len(marks)
        print(f"{sname} with id {sid} secured {percent}% ")

student_details(101,"john",87,67,89,90)
student_details(104,"sooji",79,67,89,36)
student_details(105,"john",90,90,90,90)
student_details(109,"messy")
