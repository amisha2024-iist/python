import re
s1="python is a programming Language"

#[a-z],[A-Z]

"""pat=r"old\new"
print(pat)"""

#match_obj=re.search
pat=r"[A-Z][a-z][a-z]"
match_obj=re.search(pat,s1)
print(match_obj)

#\d and \D
#\d matches 1 digit character.it is similar to [5-9
pat=r"[A-Z][a-z][a-z]\d"
match_obj=re.search(pat,s1)
print(match_obj)

#\s,\S
#\s matches aby whitespace character.
pat=r"[A-Z][a-z][a-z]\s"
match_obj=re.search(pat,s1)
print(match_obj)

s2=("""Hello there!"
     we are learning python""")
pat=r"[A-Z][a-z][a-z]\s"
match_obj=re.search(pat,s2)
print(match_obj)


