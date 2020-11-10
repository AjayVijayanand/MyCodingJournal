from random import *
import time

Team1 = []
IRUN1 = []
IBall1 = []

TRUN1 = 0
Wicket1 = 0
TBalls1 = 0

Team2 = []
IRUN2 = []
IBall2 = []

TRUN2 = 0
Wicket2 = 0
TBalls2 = 0

ScoreCardLimit = False

print("WELCOME TO BOOK CRICKET SIMULATOR")
print()
ValidInput = False
while not ValidInput:
    try:
        Players = int(input("Enter Number of Players in each side: "))
        if Players > 1:
            ValidInput = True
        else:
            print("Enter Valid Number")
    except ValueError:
        print("Enter Valid Value")
    
print()
N1 = str(input("Enter Name of Team 1: "))
Name1 = N1.upper()

for i in range(0, Players):
    NamesTeam1 = str(input("Enter Name of Player of Team 1: "))
    Team1.append(NamesTeam1)

print()
N2 = str(input("Enter Name of Team 2: "))
Name2 = N2.upper()

for i in range(0, Players):
    NamesTeam2 = str(input("Enter Name of Player of Team 2: "))
    Team2.append(NamesTeam2)

print()
print("WELCOME TO " + Name1 + " VS " + Name2)
time.sleep(3)
Toss = randint(0, 1)
Choose = randint(0, 1)
print()

if Toss == 0:
    print(Name1 + " WON THE TOSS")
    if Choose == 0:
        print("THEY HAVE CHOOSEN TO BAT FIRST")
        ChooseTeam1 = "BAT"
        ChooseTeam2 = "BOWL"
    else:
        print("THEY HAVE CHOOSEN TO BOWL FIRST")
        ChooseTeam1 = "BOWL"
        ChooseTeam2 = "BAT"
else:
    print(Name2 + " WON THE TOSS")
    if Choose == 0:
        print("THEY HAVE CHOOSEN TO BAT FIRST")
        ChooseTeam2 = "BAT"
        ChooseTeam1 = "BOWL"
    else:
        print("THEY HAVE CHOOSEN TO BOWL FIRST")
        ChooseTeam2 = "BOWL"
        ChooseTeam1 = "BAT"

print()
time.sleep(3)
print("SO, ")
print(Name1 + " WILL " + ChooseTeam1)
print(Name2 + " WILL " + ChooseTeam2)
time.sleep(3)



if ChooseTeam1 == "BAT":
    while Wicket1 <= (Players - 1):
        print()
        print(Team1[Wicket1] + " IS BATTING")
        time.sleep(3)
        Runs = 1
        Balls = 0
        IndScore = 0
        while Runs != 0:
            Runs = randint(0, 6)
            IndScore = IndScore + Runs
            TRUN1 = TRUN1 + Runs
            Balls = Balls + 1
            TBalls1 = TBalls1 + 1
            time.sleep(2)
            if 1 <= Runs <= 3:
                print("Ball " + str(Balls) + ": HE TAKES A QUICK " + str(Runs))
            elif Runs == 4 or Runs == 6:
                print("Ball " + str(Balls) + ": HE HITS A " + str(Runs))
            elif Runs == 5:
                print("Ball " + str(Balls) + ": OH NO! ITS AN OVERTHROW! " + str(Runs) + " RUNS")
            else:
                print("Ball " + str(Balls) + ": GOT 'EM!")
        time.sleep(3)
        IRUN1.append(IndScore)
        IBall1.append(Balls)
        print()
        print(Team1[Wicket1] + " IS OUT FOR " + str(IndScore) + " IN " + str(Balls) + " BALLS")
        Wicket1 = Wicket1 + 1
        time.sleep(3)
        print()
        print(Name1 + " SCORE IS " + str(TRUN1))
        print("BALLS " + str(TBalls1))
        print(Name1 + " LOST " + str(Wicket1) + " WICKETS")
    
    time.sleep(10)
    print()
    print("1ST INNING IS OVER!")
    print(Name1 + ": " + str(TRUN1))
    print(Name2 + " NEEDS " + str(TRUN1 + 1) + " TO WIN WITH " + str(Players) + " WICKETS REMAINING")

    while TRUN2 < TRUN1 and  Wicket2 <= (Players - 1):
        print()
        print(Team2[Wicket2] + " IS BATTING")
        time.sleep(3)
        Runs = 1
        Balls = 0
        IndScore = 0
        while Runs != 0:
            Runs = randint(0, 6)
            IndScore = IndScore + Runs
            TRUN2 = TRUN2 + Runs
            Balls = Balls + 1
            TBalls2 = TBalls2 + 1
            time.sleep(2)
            if 1 <= Runs <= 3:
                print("Ball " + str(Balls) + ": HE TAKES A QUICK " + str(Runs))
            elif Runs == 4 or Runs == 6:
                print("Ball " + str(Balls) + ": HE HITS A " + str(Runs))
            elif Runs == 5:
                print("Ball " + str(Balls) + ": OH NO! ITS AN OVERTHROW! " + str(Runs) + " RUNS")
            else:
                print("Ball " + str(Balls) + ": GOT 'EM!")
            if TRUN2 > TRUN1:
                break
        time.sleep(3)
        IRUN2.append(IndScore)
        IBall2.append(Balls)
        if Runs == 0:
            print()
            print(Team2[Wicket2] + " IS OUT FOR " + str(IndScore) + " IN " + str(Balls) + " BALLS")
            Wicket2 = Wicket2 + 1
            time.sleep(3)
            print()
            print(Name2 + " SCORE IS " + str(TRUN2))
            print("BALLS " + str(TBalls2))
            print(Name2 + " LOST " + str(Wicket2) + " WICKETS")
        else:
            print()
            print(Team2[Wicket2] + " SCORED " + str(IndScore) + " IN " + str(Balls) + " BALLS")
            print(Name2 + " SCORE IS " + str(TRUN2))
            print("BALLS " + str(TBalls2))

    time.sleep(10)
    print()
    print("MATCH OVER!")
    if TRUN1 < TRUN2: 
        WinningMargin = Players - Wicket2
        print(Name2 + " WON THE MATCH BY " + str(WinningMargin) + " WICKETS")
        ScoreCardLimit = True
    elif TRUN1 > TRUN2:
        WinningMargin = TRUN1 - TRUN2
        print(Name1 + " WON THE MATCH BY " + str(WinningMargin) + " RUNS")
    elif TRUN1 == TRUN2:
        print("SCORES ARE TIED!")
    
    time.sleep(3)
    print()    
    print(Name1 + " SCORECARD")
    time.sleep(1)
    for x in range(0, Wicket1):
        time.sleep(1)
        print(str(Team1[x].upper()) + " SCORED " + str(IRUN1[x]) + " RUNS IN " + str(IBall1[x]) + " BALLS")
    
    time.sleep(3)
    print()    
    print(Name2 + " SCORECARD")
    time.sleep(1)
    for x in range(0, Wicket2):
        time.sleep(1)
        print(str(Team2[x].upper()) + " SCORED " + str(IRUN2[x]) + " RUNS IN " + str(IBall2[x]) + " BALLS")




elif ChooseTeam1 == "BOWL":
    while Wicket2 <= (Players - 1):
        print()
        print(Team2[Wicket2] + " IS BATTING")
        time.sleep(3)
        Runs = 1
        Balls = 0
        IndScore = 0
        while Runs != 0:
            Runs = randint(0, 6)
            IndScore = IndScore + Runs
            TRUN2 = TRUN2 + Runs
            Balls = Balls + 1
            TBalls2 = TBalls2 + 1
            time.sleep(2)
            if 1 <= Runs <= 3:
                print("Ball " + str(Balls) + ": HE TAKES A QUICK " + str(Runs))
            elif Runs == 4 or Runs == 6:
                print("Ball " + str(Balls) + ": HE HITS A " + str(Runs))
            elif Runs == 5:
                print("Ball " + str(Balls) + ": OH NO! ITS AN OVERTHROW! " + str(Runs) + " RUNS")
            else:
                print("Ball " + str(Balls) + ": GOT 'EM!")
        time.sleep(3)
        IRUN2.append(IndScore)
        IBall2.append(Balls)
        print()
        print(Team2[Wicket2] + " IS OUT FOR " + str(IndScore) + " IN " + str(Balls) + " BALLS")
        Wicket2 = Wicket2 + 1
        time.sleep(3)
        print()
        print(Name2 + " SCORE IS " + str(TRUN2))
        print("BALLS " + str(TBalls2))
        print(Name2 + " LOST " + str(Wicket2) + " WICKETS")
    
    time.sleep(10)
    print()
    print("1ST INNING IS OVER!")
    print(Name2 + ": " + str(TRUN2))
    print(Name1 + " NEEDS " + str(TRUN2 + 1) + " TO WIN WITH " + str(Players) + " WICKETS REMAINING")

    while TRUN1 < TRUN2 and  Wicket1 <= (Players - 1):
        print()
        print(Team1[Wicket1] + " IS BATTING")
        time.sleep(3)
        Runs = 1
        Balls = 0
        IndScore = 0
        while Runs != 0:
            Runs = randint(0, 6)
            IndScore = IndScore + Runs
            TRUN1 = TRUN1 + Runs
            Balls = Balls + 1
            TBalls1 = TBalls1 + 1
            time.sleep(2)
            if 1 <= Runs <= 3:
                print("Ball " + str(Balls) + ": HE TAKES A QUICK " + str(Runs))
            elif Runs == 4 or Runs == 6:
                print("Ball " + str(Balls) + ": HE HITS A " + str(Runs))
            elif Runs == 5:
                print("Ball " + str(Balls) + ": OH NO! ITS AN OVERTHROW! " + str(Runs) + " RUNS")
            else:
                print("Ball " + str(Balls) + ": GOT 'EM!")
            if TRUN1 > TRUN2:
                break
        time.sleep(3)
        IRUN1.append(IndScore)
        IBall1.append(Balls)
        if Runs == 0:
            print()
            print(Team1[Wicket1] + " IS OUT FOR " + str(IndScore) + " IN " + str(Balls) + " BALLS")
            Wicket1 = Wicket1 + 1
            time.sleep(3)
            print()
            print(Name1 + " SCORE IS " + str(TRUN1))
            print("BALLS " + str(TBalls1))
            print(Name1 + " LOST " + str(Wicket1) + " WICKETS")
        else:
            print()
            print(Team1[Wicket1] + " SCORED " + str(IndScore) + " IN " + str(Balls) + " BALLS")
            print(Name1 + " SCORE IS " + str(TRUN1))
            print("BALLS " + str(TBalls1))

    time.sleep(10)
    print()
    print("MATCH OVER!")
    if TRUN2 < TRUN1: 
        WinningMargin = Players - Wicket2
        print(Name1 + " WON THE MATCH BY " + str(WinningMargin) + " WICKETS")
        ScoreCardLimit = True
    elif TRUN2 > TRUN1:
        WinningMargin = TRUN2 - TRUN1
        print(Name2 + " WON THE MATCH BY " + str(WinningMargin) + " RUNS")
    elif TRUN1 == TRUN2:
        print("SCORES ARE TIED!")
    
    time.sleep(3)
    print()    
    print(Name2 + " SCORECARD")
    time.sleep(1)
    for x in range(0, Wicket2):
        time.sleep(1)
        print(str(Team2[x].upper()) + " SCORED " + str(IRUN2[x]) + " RUNS IN " + str(IBall2[x]) + " BALLS")
    
    time.sleep(3)
    print()    
    print(Name1 + " SCORECARD")
    time.sleep(1)
    for x in range(0, Wicket1):
        time.sleep(1)
        print(str(Team1[x].upper()) + " SCORED " + str(IRUN1[x]) + " RUNS IN " + str(IBall1[x]) + " BALLS")