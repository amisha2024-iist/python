student1={"maths":80.5,"eng":76.0,"phy":89}
print(student1)
#fetch the marks of "phy"
print(student1["phy"])
print(student1["eng"])

#get
print(student1.get("phy"))
print(student1.get("chem"))#gives output as none.
employ1={'id':1001,'name':'john','salary':10000}
print(employ1)
print(employ1.get('id',9938788849))#it will give the real id =1001.

#membership operator=>in
print(1001 in employ1)#it gives false because yes it is present in the dictionary but not as an element it is present as a value.
print('name' in employ1)
employ1['phone']=9920444983#added phone in dictionary
print(employ1)

sem1_marks={'maths':90,'eng':45,'phy':70,'chem':80}
sem2_marks={'chem':89,'bio':78}

sem1_marks.update(sem2_marks)
print(sem1_marks)

sem1_marks.pop('chem')
print(sem1_marks)

#keys can not be duplicate in a dictionary but only canbe updated.


