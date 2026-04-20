#sets are another datatype
#sets are collection of items
#they are non sequential collection
#comma separated statement enclosed within {}

set1={10,"python",3.9}
print(set1)
print(type(set1))

#comma have indexing with sets
#print(set1[0])#gives error because indexing and slicing are not allowed in set
print(len(set1))
#we need sets because in list and tuple we can have duplicate element but in sets duplicate elements are not allowed.
l1=[10,30,40,30,40]
print(l1,type(l1))
s1={1,2,1,3,5,2}
print(s1,type(s1))
