import random

lower_limit = int(input("Choose your lower limit: "))
higher_limit = int(input("Choose your higher limit: "))
random_int = random.randint(lower_limit, higher_limit)
guess = 0

while guess != random_int:
    guess = int(input("Guess the number: "))
    if guess < random_int:
        print("Too low, try again")
    elif guess > random_int:
        print("Too high, try again")
    else:
        print('\n')
        print("You win! 😃")