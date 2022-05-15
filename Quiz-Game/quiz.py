print(" Hi! .. Lets play  the quiz Game")

player1 = input(" Do you want to play? ")

if player1.lower() != "yes":
    quit()

print(" Okay, Lets play ")
score = 0

answer = input(" What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input(" What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input(" What does RAM stand for? ")
if answer.lower() == " random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input(" What does PS stand for? ")
if answer.lower() == "play station":
    print("correct")
    score += 1
else:
    print("incorrect")


print(" You get " + str(score) + " quesion correct")
print(" You get " + str((score/4) * 100) + "%")
