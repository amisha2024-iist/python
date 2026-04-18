"""s1="python is fun"
print(s1[0])
print(len(s1))
language=("python")
version="3.13.3"
print(language+version)"""
#s1="python"
#print(s1 * 10)#in strings '*'is repetition operator""".
#membersship operation
#in operator
s1="python is fun"
print("python" in s1)#gives true
print("i" in s1)#gives true
print("apple"in s1) #gives false

#not in operator
s2="aur bhai kya hal chal"
print("bhai" not in s2)
print("bhai" not in s1)

#comparision operator
print("python"=="python")
#removing spaces from a string = stipe()
s3=("    python          ")
print(s3)
print(s3.strip()=="python")

#replace
s4="i love python programming"
print(s4)
print(s4.replace("python","java"))
print(s4.replace("e","E"))
print(s4.replace("e","E",1))
