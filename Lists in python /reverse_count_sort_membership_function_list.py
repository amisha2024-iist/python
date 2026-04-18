"""
reverse
sort
count
membership
"""
"""reverse()
sort()
count()
membership"""
from itertools import count

days_of_week=["monday","tuesday","wednesday","thursday"]
print(days_of_week)
#reverse
days_of_week.reverse()
print(days_of_week)
#sort
nums=[3,6,2,6,8,34,56,7]
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)#sorted list will be in descending order.
print(nums)
#count():count any particular element repetition in a list
numbers=[0,1,3,4,5,3,5,2,0,7,0,7,0]
print(f"the list is: {numbers}")
item_to_count=int(input("enter the nummber to count"))
c=numbers.count(item_to_count)
print(f"occurrence of {item_to_count} is {c}")
#membership operation
#in:it check whether the element is present or not in a list.
language=["python","c++","java","python"]
print("python" in language)
print("javascript" not in language)
