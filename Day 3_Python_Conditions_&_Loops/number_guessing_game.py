import random

num= random.randint(1, 50)
attempt=0

while True:
    guess = int(input("guess the number between 1 to 50: "))
    attempt = attempt + 1

    if guess > num:
        print("number is too high")

    elif guess < num:
        print("number is too low")
    else:
        print("your guess it right in", attempt, "attempts")
        break        