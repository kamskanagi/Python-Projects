import random

top_of_range = input(" Type a number")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than zero (0) ")
        quit()

else:
    print("Please type a number")
    quit()


randon_number = random.randrange(0, top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number")
        continue
    if user_guess == randon_number:
        print("You get it right")
        break
    else:
        if user_guess > randon_number:
            print(" You were above the number")
        else:
            print(" You were below the number")


print("You get it in", guess, "guesses")
