# Игра по угадыванию чисел
import random

guesses_taken = 0

print("Hello, whats your name?")
player_name = input("Type it here!")

number = random.randint(1, 20)
print(f"Well, {player_name}, i will guess the number between 1 and 20, try to get it in lestt tries that you could! ")

for guesses_taken in range(6):
    guess = input()
    guess = int(guess)

    if guess < number:
        print(f"Hey {player_name}, your number is too small")

    if guess > number:
        print(f"Hey {player_name} your number is too big")

    if guess == number:
        guesses_taken = str(guesses_taken + 1)
        print(f"Nice {player_name}, you did it in {guesses_taken} times!")
    
if guess != number:
    print(f"{player_name} you are not right, my number was {number}")
