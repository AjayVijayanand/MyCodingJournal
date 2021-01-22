from random import *

def RPS(C, User):
    if C == 1:
        print(User + " Choose Rock")
    elif C == 2:
        print(User + " Choose Paper")
    elif C == 3:
        print(User + " Choose Scissors")

YOU = 0
COMP = 0
Choice = 1
while Choice != 0:
    Choice = int(input("Inupt Your Choices (|Rock - 1|Paper - 2|Scissors - 3|Exit - 0): "))
    CompChoice = randint(1, 3)
    print()
    if Choice != 0:
        RPS(Choice, "You")
        RPS(CompChoice, "Computer")
        if Choice == 2 and CompChoice == 1:
            print("YOU HAVE GOT THE POINT!")
            YOU =+ 1
        elif Choice == 1 and CompChoice == 2:
            print("COMPUTER HAS GOT THE POINT!")
            COMP =+ 1
        elif Choice == 3 and CompChoice == 2:
            print("YOU HAVE GOT THE POINT!")
            YOU =+ 1
        elif Choice == 2 and CompChoice == 3:
            print("COMPUTER HAS GOT THE POINT!") 
            COMP =+ 1
        elif Choice == 1 and CompChoice == 3:
            print("YOU HAVE GOT THE POINT!")
            YOU =+ 1
        elif Choice == 3 and CompChoice == 1:
            print("COMPUTER HAS GOT THE POINT!")
            COMP =+ 1
        else:
            print("ITS A TIE")

print("Game Over")
if YOU > COMP:
    print("YOU WIN!")
elif YOU < COMP:
    print("COMPUTER WINS!")
else:
    print("ITS A DRAW")
print("YOU: " + str(YOU))
print("COMPUTER: " + str(COMP))