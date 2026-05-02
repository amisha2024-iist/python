"""
create a simple number guessing game.
the user geta 10 chances to guess a number.
if the user guesses the number before 10 characters,stop asking the number from the user,say congrats and end the game.
if the user never guesses the number,ask them 10 times and then end the game!
"""
import random
num=1
print("welcome to the number guessing game,you have 10 chances to guess a number.")
print("the secret number is between 1-90")
secret_number=78
attempts=10

while num<=10:
    user_number=int(input("enter your guess:"))
    if user_number==secret_number:
        print("your guess is correct!,congrats")
        break
    else:
        if user_number<secret_number:
            higher_or_lower='higher'
            print(f"your guess is wrong,try higher number {higher_or_lower}")

        else:
            higher_or_lower='lower'
            print(f"your guess is wrong,try lower number {higher_or_lower}")

    num=num+1
