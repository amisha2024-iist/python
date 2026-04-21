#frozen sets-immutable sets
fs1=frozenset({10,30,20})
print(fs1,type(fs1))

"""fs1.add(40)
print(fs1)#gives an error(frozenset object has no attributes 'add"""

fs2=frozenset({10,30,50,100})
print(fs2,type(fs2))

print(fs1|fs2)
print(fs1-fs2)
