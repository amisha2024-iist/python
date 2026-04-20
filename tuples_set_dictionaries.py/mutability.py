#Mutability and Immutability
#Mutability is the ability of a value or a data to be modifies or change
#Immutability is the inability of some data to be changed (reverse of mutability)
#lists are mutable
#tuples and strings are immutable
s1="python is fun"
s2=s1.replace("python","java")
print(s2)
#in string replace function doesn't replace the actual string it gives us another new value of the string.
l1=["mango","orange","apple"]
l1.append("banana")
print(l1)
#to check the memory address we use id function
#id of l1 before the change is done and id of l1 after the change is done.
print(id(l1))#before changing id of l1=199-------464
l1[-1]="apple"
print(l1)
print(id(l1))#after change id of l1=199---------464
#so mutability is :if a datatype is able to change the state of it's own without changing the memory address of itself.
#but tuple can not do this
fruits=("apple","mango","orange")
print(fruits)
fruits[-1]="orange"
print(fruits)#it will give an error because the state of a tuple can not be change after it created.
#same happens with the strings only lists are mutable.
