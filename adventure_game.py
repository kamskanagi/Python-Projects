name = input(" Enter your name ")
print("Welcome to the adventure game", name)

answer = input("You are on a dirt road, you can go left or right ? ").lower()

if answer == "left":
    answer = input(
        " You come the the river, you can walk around it or swin across? Type walk to walk around and swim to swim across").lower()

    if answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    elif answer == "swim":
        print("You swin across and eaten by an alligator.")

    else:
        print(" Not a valid option. You lose")

elif answer == "right":
    answer = input(
        "You camoe to a brideg, it look wobbly, do you want to corss it? cross or back?").lower()

    if answer == "back":
        print("You go back and lose")
    elif answer == "swim":
        answer = input(
            " You corss the bridge and meet a stranger. Do you talk? yes or no ").lower()

        if answer == "yes":
            print("You talk to the starnger and they give you Gold. You win")
        elif answer == "no":
            print("You ignore the stranger and they are offended, you lose!")
        else:
            print(" Not a valid option. You lose")

    else:
        print(" Not a valid option. You lose")

else:
    print(" not a valid option. You Lost")


print(" Thank you", name)
