scores=[0,2,5,56,34,78,35,67,23,56,7]
"""total=0
for score in scores:
    total = total+score"""

#total=sum(scores)
#print("total run score is",total)
#either we can use a for loop or sum variable both work same here for adding the element.
#to find the highest score
"""highest=scores[0]
for score in scores:
    if highest<score:
        highest = score
print(highest)"""
#instead of using for loop we have a function in python that is max.
highest=max(scores)
print(f"highest score is",{highest})

lowest=min(scores)
print(f"lowest score is",{lowest})
