#comma separated key-vale pairs enclosed wothin{}
#{key1:value1,key2:value2,......}

groceries={'milk':60,'biscuits':70,'eggs':80}
print(groceries)
print(type(groceries))
print(len(groceries))
#print(groceries[0])#gives an error bcs it doesn't have indexes.
#so to fetch the value we have keys.
print(groceries['milk'])
print(groceries['eggs'])
#dictionaries are mutable
groceries['milk']=80
print(groceries)
#add new key value pair in dictionary.
groceries['rice']=50
print(groceries)
