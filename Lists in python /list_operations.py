"""#slicing of list
l1=[2,3,5,6,7,8,4,6]
print(l1[1:6:1])
print(l1[0:7:3])
print(l1[-1:6:-1])

#concatination of list
l2=[4,6,7]
print(l1+l2)
print(l2+l1)
#reperirion of list
# *
print(l2*3)
print(l1*2)"""
#append of a list
#adds an item to the end of a list
fruits=['apple','banana','orange']
print(fruits)
#syntax:list.append()
fruits.append('pear')
print(fruits)

#insert
#adds an element before the specified index
fruits.insert(2,"mango") #mango will add before the second index
print(fruits)
