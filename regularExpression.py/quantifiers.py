import re
message=" The current Python version is 3.13,other previous version of python are 3.10,3.12,3.11."

pat=r"[a-z]{4}"
match_obj=re.search(pat,message)
print(match_obj)

pat=r"[A-Z][a-z]{5}"
match_obj=re.search(pat,message)
print(match_obj)

pat=r"[A-Z][a-z]{1,5}"
match_obj=re.search(pat,message)
print(match_obj)

#+=> matches 1 or more repetitions of the previous pattern.
pat=r"[A-Z][a-z]+"
match_obj=re.search(pat,message)
print(match_obj)

#? => 0 or1 repetitions of the previous pattern
pat=r"[A-Z][a-z]?"
match_obj=re.search(pat,message)
print(match_obj)

#* => 0 or more repetition of the previous pattern.
pat=r"[A-Z][a-z]*"
match_obj=re.search(pat,message)
print(match_obj)
