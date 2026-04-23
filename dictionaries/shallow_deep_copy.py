#these concepts are for mutable datatype.
import copy

l1=[1,3,4,[10,40,30],'python']

#shallow copy
#l2=copy.copy(l1)
"""print(l2)
print(id(l1))
print(id(l2))"""

"""l1[0]=100
print(f"l1->{l1}",id(l1))#will replace the 0th index element with 100
print(f"l2->{l2}",id(l2))#remains unchanged.

l1[3][0]=50
print(f"l1->{l1}",id(l1))
print(f"l2->{l2}",id(l2))"""

#deep copy:only change the  duplicate one not the original one.
l2=copy.deepcopy(l1)
l1[0]=100
l1[3][0]=50
print(f"l1->{l1}",id(l1))
print(f"l2->{l2}",id(l2))
#also work for dictionary
d1={'id':1020,'name':'john','marks': {'eng':70.5,'phy':60}}
#deep copy
d2=copy.deepcopy(d1)
d1['marks']['phy']=80
print(f"d1->{d1}",id(d1))
print(f"d2->{d2}",id(d1))

