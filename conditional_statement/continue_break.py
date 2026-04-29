"""for num in range(10):
    if num % 3 == 0: #if the number is divisible by 3
        continue

    print(num)"""
for num in range(1,10):
    if num % 3 == 0: #if the number is divisible by 3
        break
#when it comes to any number divisible by 3 in the given range it will break(stop).
    print(num)
