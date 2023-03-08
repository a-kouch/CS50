import random
import sys

level = random.randint(1, 5)
print("Level: " + str(level))
guess = int(input("Guess: "))

while True:
    if guess < level:
        print("Too small!")
        guess = int(input("Guess: "))
    elif guess > level:
        print("Too large!")
        guess = int(input("Guess: "))
    else:
        print("Just right!")
        break