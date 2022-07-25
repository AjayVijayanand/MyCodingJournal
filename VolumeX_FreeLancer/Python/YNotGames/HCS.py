from random import *
import time

TRUN1 = 0
Wickets1 = 0
TBalls1 = 0

TRUN2 = 0
TBalls2 = 0
Wickets2 = 0

print()
print("WELCOME TO THE HAND CRICKET SIMULATOR")
print()
time.sleep(1)
ValidInput1 = False
while not ValidInput1:
    try:
        Toss = int(input("Odd(0) or Ev(1)?: "))
        if Toss == 0 or Toss == 1:
            ValidInput1 = True
        else:
            print("Enter valid choice")
    except ValueError:
        print("Enter Valid Value")

ValidInput2 = False
while not ValidInput2:
    try:
        RunToss = int(input("Enter Number: "))
        if 0 < RunToss <= 6:
            ValidInput2 = True
        else:
            print("Enter valid run")
    except ValueError:
        print("Enter Valid Value")

MRunToss = randint(1, 6)
ResToss = MRunToss + RunToss

time.sleep(1)
print()
print("Your Choice: " + str(RunToss))
print("Computer Choice: " + str(MRunToss))
print()
time.sleep(1)

if Toss == 0:
    if (ResToss % 2) == 1:
        print("YOU WON THE TOSS")
        C, U = False, True
    else:
        print("COMPUTER WON THE TOSS")
        C, U = True, False
else:
    if (ResToss % 2) == 0:
        print("YOU WON THE TOSS")
        C, U = False, True
    else:
        print("COMPUTER WON THE TOSS")
        C = True
        C, U = True, False

time.sleep(1)
if U:
    ValidInput3 = False
    while not ValidInput3:
        try:
            Choose = int(input("What do you want to choose (1 - Bat | 0 - Bowl): "))
            if Choose == 1 or Choose == 0:
                ValidInput3 = True
            else:
                print("Enter valid run")
        except ValueError:
            print("Enter Valid Value")
        time.sleep(1)
        if Choose == 1:
            print("YOU CHOOSE TO BAT")
            ChooseTeamC, ChooseTeamU  = "BOWL", "BAT"
        else:
            print("YOU CHOOSE TO BOWL")
            ChooseTeamC, ChooseTeamU  = "BAT", "BOWL"
        time.sleep(1)
        ValidInput4 = False
        while not ValidInput4:
            try:
                Wickets = int(input("How many wickets: "))
                if 0 < Wickets <= 10:
                    ValidInput4 = True
                else:
                    print("Enter valid run")
            except ValueError:
                print("Enter Valid Value")
else:
    Choose = randint(0, 1)
    if Choose == 0:
        print("COMPUTER CHOOSE TO BOWL")
        ChooseTeamC, ChooseTeamU  = "BOWL", "BAT"
    else:
        print("COMPUTER CHOOSE TO BAT")
        ChooseTeamC, ChooseTeamU  = "BAT", "BOWL"
    Wickets = randint(1, 10)
time.sleep(1)
print("FOR " + str(Wickets) + " WICKET(S)")

time.sleep(1)
print()
print("SO, ")
print("YOU WILL " + ChooseTeamU)
print("THE COMPUTER WILL " + ChooseTeamC)
print("THIS MATCH IS FOR " + str(Wickets) + " WICKET(S)")
print()
time.sleep(1)

print()
if ChooseTeamU == "BAT":
    print()
    print("YOU ARE NOW BATTING.")
    print()
    time.sleep(1)
    while Wickets1 <= (Wickets - 1):
        Balls = 0
        Out = False
        while not Out:
            print()
            ValidInput5 = False
            while not ValidInput5:
                try:
                    Runs = int(input("What is your run choice: "))
                    if 0 < Runs <= 6:
                        ValidInput5 = True
                    else:
                        print("Enter valid run (Number MUST be from 1 to 6")
                except ValueError:
                    print("Enter Valid Value")
            print()
            time.sleep(1)
            CompRuns = randint(1, 6)
            print("Your Choice: " + str(Runs))
            print("Computer's Choice: " + str(CompRuns))
            Balls = Balls + 1
            TBalls1 = TBalls1 + 1
            print()
            time.sleep(1)
            if CompRuns != Runs:
                TRUN1 = TRUN1 + Runs
                if 1 <= Runs <= 3:
                    print("Ball " + str(Balls) + " He takes a quick " + str(Runs))
                elif Runs == 4 or Runs == 6:
                    print("Ball " + str(Balls) + " He hits a " + str(Runs))
                elif Runs == 5:
                    print("Ball " + str(Balls) + " Oh no! It is an overthrow " + str(Runs) + " Runs.")
            else:
                print("Ball " + str(Balls) + " GOT 'EM")
                Out = True

        print()
        time.sleep(1)
        Wickets1 = Wickets1 + 1
        print("Your Score: " + str(TRUN1))
        print("Balls: " + str(TBalls1))
        print("You lost " + str(Wickets1) + " Wickets")

    print()
    print()
    time.sleep(1)
    time.sleep(1)
    print("1st innings is over.")
    print("You Scored: " + str(TRUN1))
    print("Computer Needs " + str(TRUN1 + 1) + " to win with " + str(Wickets) + " wicket(s) remaining")

    print()
    print("COMPUTER IS NOW BATTING.")
    print()
    time.sleep(1)
    while TRUN2 <= TRUN1 and Wickets2 <= (Wickets - 1):
        Balls = 0
        Out2 = False
        while not Out2:
            print()
            ValidInput6 = False
            while not ValidInput6:
                try:
                    Runs = int(input("What is your Ball choice: "))
                    if 0 < Runs <= 6:
                        ValidInput6 = True
                    else:
                        print("Enter valid ball (Number MUST be from 1 to 6")
                except ValueError:
                    print("Enter Valid Value")
            print()
            time.sleep(1)
            CompRuns = randint(1, 6)
            print("Your Choice: " + str(Runs))
            print("Computer's Choice: " + str(CompRuns))
            Balls = Balls + 1
            TBalls2 = TBalls2 + 1
            print()
            time.sleep(1)
            if CompRuns != Runs:
                TRUN2 = TRUN2 + CompRuns
                if 1 <= CompRuns <= 3:
                    print("Ball " + str(Balls) + " He takes a quick " + str(CompRuns))
                elif CompRuns == 4 or CompRuns == 6:
                    print("Ball " + str(Balls) + " He hits a " + str(CompRuns))
                elif CompRuns == 5:
                    print("Ball " + str(Balls) + " Oh no! It is an overthrow " + str(CompRuns) + " Runs.")
            else:
                print("Ball " + str(Balls) + " GOT 'EM")
                Out2 = True
            if TRUN2 > TRUN1:
                Out2 = True
                break
        print()
        time.sleep(1)
        if CompRuns == Runs:
            Wickets2 = Wickets2 + 1
            print("Computer's Score: " + str(TRUN2))
            print("Balls " + str(TBalls2))
            print("Computer needs " + str((TRUN1 + 1) - TRUN2) + " with " + str(Wickets - Wickets2) + " Remaining")
        else:
            print("Computer's Score: " + str(TRUN2))
            print("Balls " + str(TBalls2))

    print()
    print()
    time.sleep(1)
    time.sleep(1)
    print("Match Over")
    print()
    time.sleep(1)

    if TRUN1 < TRUN2:
        WinningMarg = Wickets - Wickets2
        print("COMPUTER WON THE MATCH BY " + str(WinningMarg) + " WICKETS")
    elif TRUN1 > TRUN2:
        WinningMarg = TRUN1 - TRUN2
        print("YOU WON THE MATCH BY " + str(WinningMarg) + " RUNS")
    elif TRUN1 == TRUN2:
        print("SCORES ARE TIED.")

    print()
    time.sleep(1)
    print("YOU: " + str(TRUN1))
    print("COMPUTER: " + str(TRUN2))

elif ChooseTeamU == "BOWL":
    print()
    print("COMPUTER IS NOW BATTING.")
    print()
    time.sleep(1)
    while Wickets1 <= (Wickets - 1):
        Balls = 0
        Out = False
        while not Out:
            print()
            ValidInput5 = False
            while not ValidInput5:
                try:
                    Runs = int(input("What is your ball choice: "))
                    if 0 < Runs <= 6:
                        ValidInput5 = True
                    else:
                        print("Enter valid ball (Number MUST be from 1 to 6")
                except ValueError:
                    print("Enter Valid Value")
            print()
            time.sleep(1)
            CompRuns = randint(1, 6)
            print("Your Choice: " + str(Runs))
            print("Computer's Choice: " + str(CompRuns))
            Balls = Balls + 1
            TBalls1 = TBalls1 + 1
            print()
            time.sleep(1)
            if CompRuns != Runs:
                TRUN1 = TRUN1 + CompRuns
                if 1 <= CompRuns <= 3:
                    print("Ball " + str(Balls) + " He takes a quick " + str(CompRuns))
                elif CompRuns == 4 or CompRuns == 6:
                    print("Ball " + str(Balls) + " He hits a " + str(CompRuns))
                elif CompRuns == 5:
                    print("Ball " + str(Balls) + " Oh no! It is an overthrow " + str(CompRuns) + " Runs.")
            else:
                print("Ball " + str(Balls) + " GOT 'EM")
                Out = True

        print()
        time.sleep(1)
        Wickets1 = Wickets1 + 1
        print("Computer's Score: " + str(TRUN1))
        print("Balls: " + str(TBalls1))
        print("Computer lost " + str(Wickets1) + " Wickets")

    print()
    print()
    time.sleep(1)
    time.sleep(1)
    print("1st innings is over.")
    print("Computer Scored: " + str(TRUN1))
    print("You Need " + str(TRUN1 + 1) + " to win with " + str(Wickets) + " wickets remaining")

    print()
    print("YOU ARE NOW BATTING.")
    print()
    time.sleep(1)
    while TRUN2 <= TRUN1 and Wickets2 <= (Wickets - 1):
        Balls = 0
        Out2 = False
        while not Out2:
            print() 
            ValidInput6 = False
            while not ValidInput6:
                try:
                    Runs = int(input("What is your run choice: "))
                    if 0 < Runs <= 6:
                        ValidInput6 = True
                    else:
                        print("Enter valid run (Number MUST be from 1 to 6")
                except ValueError:
                    print("Enter Valid Value")
            print()
            time.sleep(1)
            CompRuns = randint(1, 6)
            print("Your Choice: " + str(Runs))
            print("Computer's Choice: " + str(CompRuns))
            Balls = Balls + 1
            TBalls2 = TBalls2 + 1
            print()
            time.sleep(1)
            if CompRuns != Runs:
                TRUN2 = TRUN2 + Runs
                if 1 <= Runs <= 3:
                    print("Ball " + str(Balls) + " He takes a quick " + str(Runs))
                elif Runs == 4 or CompRuns == 6:
                    print("Ball " + str(Balls) + " He hits a " + str(Runs))
                elif Runs == 5:
                    print("Ball " + str(Balls) + " Oh no! It is an overthrow " + str(Runs) + " Runs.")
            else:
                print("Ball " + str(Balls) + " GOT 'EM")
                Out2 = True
            if TRUN2 > TRUN1:
                Out2 = True
                break

        print()
        time.sleep(1)
        if CompRuns == Runs:
            Wickets2 = Wickets2 + 1
            print("Your Score: " + str(TRUN2))
            print("Balls " + str(TBalls2))
            print("You need " + str((TRUN1 + 1) - TRUN2) + " with " + str(Wickets - Wickets2) + " Remaining")
        else:
            print("Your Score is " + str(TRUN2))
            print("Balls " + str(TBalls2))

    print()
    print()
    time.sleep(1)
    time.sleep(1)
    print("Match Over")
    print()
    time.sleep(1)

    if TRUN1 < TRUN2:
        WinningMarg = Wickets - Wickets2
        print("YOU WON THE MATCH BY " + str(WinningMarg) + " WICKETS")
    elif TRUN1 > TRUN2:
        WinningMarg = TRUN1 - TRUN2
        print("COMPUTER WON THE MATCH BY " + str(WinningMarg) + " RUNS")
    elif TRUN1 == TRUN2:
        print("SCORES ARE TIED.")

    print()
    time.sleep(1)
    print("COMPUTER: " + str(TRUN1))
    print("YOU: " + str(TRUN2))