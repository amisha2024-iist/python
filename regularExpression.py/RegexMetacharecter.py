import re
message ="the current version is python 3.13.the other previous versions are 3.12,3.10,3.11"

match_object=re.search("[0-9][0-9]",message)
print(match_object)

match_object=re.search("[0-9][0-9]","house number: 343/A")#print 2 conjucative numbers from the given string
print(match_object)

match_object=re.search("[0-9][0-9][0-9]","house number: 343/A")
print(match_object)

match_object=re.search("[0-9][0-9][0-9]","message")
print(match_object)

