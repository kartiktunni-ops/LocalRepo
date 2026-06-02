import random

secret_number = random.randint(1, 10)

print("🎮 Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("🎉 Correct! You win!")
else:
    print(f"😢 Nope! The number was {secret_number}.")