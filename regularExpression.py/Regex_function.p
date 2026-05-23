#match()
import re
s1=("we are learning regex in python")
pat=r"[a-z]{3}"
match_obj=re.match(pat,s1)
print(match_obj)

phones="john=2345343,carol=23532345,mark=45884355689,alice=341578345,python3.13.2"
pat=r"[0-9]+"
match_obj=re.findall(pat,phones)
print(match_obj)
#\b
#fetch all phone number .the phone number is exactly 7 digit and should not exceed 15 digit.
pat=r"[0-9]{7,15}\b"
match_obj=re.findall(pat,phones)
print(match_obj)

#fetch the phone number.the phone number are at least 7 digit.
pat=r"[0-9]{7,}"#7 or more
match_obj=re.findall(pat,phones)
print(match_obj)

#finditer()
pat=r"\b[0-9]{7,15}\b"
match_obj_iter=re.finditer(pat,phones)
for matches in match_obj_iter:
    print(matches)
