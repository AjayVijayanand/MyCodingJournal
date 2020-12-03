from random import *
from time import sleep

RunsDie = ["1", "1", "2", "2", "3", "3"]
ConservativeDie = ["Dot Ball", "Hook Shot", "Pull Shot", "Cut Shot", "Cover Drive", "Howzat?"]
AggressiveDie = ["4 Runs", "Super Shot 4", "Big Hit 6", "In the Air?", "Outsdie Edge", "Big Swing and A Miss"]
BowlingDie = ["Clean Bowled", "No Ball", "Fast Ball", "Spin", "Bouncer", "Swing Ball"]
FieldingDie = ["Through the Gap", "Over the Top", "Dropped Catch", "Fielded", "Classic Catch", "Shot at the stumps"]
UmpireDie = ["Not Out", "LBW", "Caught and Bowled", "Run Out", "Caught", "Not Out"]

Run1 = 0
Run2 = 0

PlayerChoice1 = ""
PlayerChoice2 = ""

ChoiceValid = False

Out = False
PlayerScore1 = 0
PlayerBalls1 = 0
PlayerScore2 = 0
PlayerBalls2 = 0

def CD(DieResult, FreeHit):
    if ConservativeDie[DieResult] == "Dot Ball":
        print("Batsman left the ball. No Run")
        if FreeHit:
            print("What is the batsman thinkning!? It's a free hit and he has left the ball! Unbeleivable!!!")
        return False, False
    elif ConservativeDie[DieResult] == "Hook Shot":
        print("Batsman has hit a hookshot! Let's see how many runs he will get!")
        return True, False
    elif ConservativeDie[DieResult] == "Pull Shot":
        print("Pull shot! Could get a couple of runs!")
        return True, False
    elif ConservativeDie[DieResult] == "Cut Shot":
        print("Cut Away! What's gonna happen!")
        return True, False
    elif ConservativeDie[DieResult] == "Cover Drive":
        print("Beautiful Shot! Has to get runs here!")
        return True, False
    elif ConservativeDie[DieResult] == "Howzat?":
        print("Big Appeal! He may be out here!")
        if FreeHit:
            print("Oh wait! It was a free hit. Oh well! It's a dot ball anyways")
            return False, False
        else:
            print("What is the Umpire gonna say about it!")
            return False, True


def AD(DieResult, PS, FreeHit):
    if AggressiveDie[DieResult] == "4 Runs":
        print("Good Timing. And it's good enough for 4!! Wow!")
        PS = PS + 4
        if FreeHit:
            print("Well he did well to make the most of the Free Hit")
        return False, PS
    elif AggressiveDie[DieResult] == "Super Shot 4":
        print("Well that has been smashed powerfully for 4. What a Shot!")
        PS = PS + 4
        if FreeHit:
            print("Good use of the free hit!")
        return False, PS
    elif AggressiveDie[DieResult] == "Big Hit 6":
        print("Well Don't worry about that. That's way over the benches!")
        PS = PS + 6
        if FreeHit:
            print("If you wanna know how to make use of a free hit. Well, this is the perfect example!")
        return False, PS
    elif AggressiveDie[DieResult] == "In the Air?":
        print("Straight up in the air! Who wants it!?")
        if FreeHit:
            print("Well it doesnt matter since it's a free hit but still saved some valuable runs!")
            return False, PS
        else:
            print("WHO WANTS IT!??")
            return True, PS
    elif AggressiveDie[DieResult] == "Outside Edge":
        print("Edged!")
        return True, PS
    elif AggressiveDie[DieResult] == "Big Swing and A Miss":
        print("Well he swings it! And misses it!")
        if FreeHit:
            print("Good attempt on the free hit though")
        return False, PS


def BD(DieResult, PS, PB):
    if BowlingDie[DieResult] == "Clean Bowled":
        print("Bowled Em!!!!")
        if PS == 0:
            print("That's not what he would have wanted. It's a duck for the batsman")
            if PB == 1:
                print("It's a Golden duck for that matter!")
        return False, True, PB, PS, False
    elif BowlingDie[DieResult] == "No Ball":
        print("Oh dear! It's a No ball! Free Hit coming up!")
        FreeHit = True
        PB = PB - 1
        PS = PS + 1
        return True, False, PB, PS, True
    elif BowlingDie[DieResult] == "Fast Ball":
        print("Bowler's bowled a Fast one!")
        return True, False, PB, PS, False
    elif BowlingDie[DieResult] == "Spin":
        print("Bowler's trying to fool the batsman with Spin")
        return True, False, PB, PS, False
    elif BowlingDie[DieResult] == "Bouncer":
        print("Woah! He's trynna give the batsman a warning with a bouncer!")
        return True, False, PB, PS, False
    elif BowlingDie[DieResult] == "Swing Ball":
        print("That Ball Swung!")
        return True, False, PB, PS, False


def FeD(DieResult1, DieResult2):
    if FieldingDie[DieResult1] == "Through the Gap":
        if AggressiveDie[DieResult2] == "Outside Edge":
            print("But it's through the gap!")
        elif AggressiveDie[Batting] == "In the Air?":
            print("But it's in no man's land so he's safe!")
        else:
            print("Good placement by the batsman, should get some runs")
        return True, False, False
    elif FieldingDie[DieResult1] == "Over the Top":
        if AggressiveDie[DieResult2] == "Outside Edge" or AggressiveDie[DieResult2] == "In the Air?":
            print("Just over the fielder's head, they gotta run hard")
        else:
            print("Lofted over the fielder. They are gonna get some runs here")
        return True, False, False
    elif FieldingDie[DieResult1] == "Dropped Catch":
        if AggressiveDie[DieResult2] == "Outside Edge":
            print("Oh dear he's dropped the catch!")
        elif AggressiveDie[DieResult2] == "In the Air?":
            print("It's Safe! He's Dropped it. That is soo unfortunate!")
        else:
            print("Oh he's dropped it that's unfortunate")
        return True, False, False
    elif FieldingDie[DieResult1] == "Classic Catch":
        if FreeHit:
            print("GONE! But it's a free hit! So that's not out.")
            return True, False, False
        elif AggressiveDie[DieResult2] == "Outside Edge":
            print("And Gone that's a wicket.")
            return False, True, False
        elif AggressiveDie[DieResult2] == "In the Air?":
            print("Great Catch from the fielder that's gone!")
            return False, True, False
        else:
            print("GONE! He's gone. What a catch!")
            return False, True, False
    elif FieldingDie[DieResult1] == "Shot at the Stumps":
        if ConservativeDie[DieResult2] == "Outside Edge" or ConservativeDie[DieResult2] == "In the Air?":
            print("Dropped but there maybe a runout chacne here! He get's a direct hit. It's going up stairs!")
        else:
            print("Good throw and that's a direct hit! He maybe out! 3rd Umpire Now Checking!")
        return False, False, True
    elif FieldingDie[DieResult1] == "Fielded":
        print("Great Fielding. No Runs!")
        return False, False, False


def UmD(DieResult, DieResult2):
    if UmpireDie[DieResult] == "Not Out":
        print("Umpire Doesn't think it's out. Well. On to the next then!")
        if FieldingDie[DieResult2] == "Shot at the Stumps":
            return True, False
    elif UmpireDie[DieResult] == "LBW" or UmpireDie[DieResult] == "Caught":
        if FieldingDie[DieResult2] == "Shot at the Stumps":
            print("Ohh Batsman's in! Not out!")
            return True, False
        else:
            print("Finger Goes Up! That's gone and the batsman will now have to walk back!")
            return False, True
    elif UmpireDie[DieResult] == "Caught and bowled":
        if FieldingDie[DieResult2] == "Shot at the Stumps":
            print("Ohh Batsman's in! Not out!")
            return True, False
        else:
            print("Great Return Catch! That's unbelievable! The batsman can't believe it! Nor can Anyone for that matter!")
            Out = True
    elif UmpireDie[DieResult] == "Run Out":
        if FieldingDie[DieResult2] == "Shot at the Stumps":
            print("And that's gone!")
        else:
            print("No hesitation there. That's out!")
        return False, True


def RuD(DieResult, PS):
    if RunsDie[DieResult] == "1":
        print("He takes a Single")
        PS = PS + 1
    elif RunsDie[DieResult] == "2":
        print("He goes for the double")
        PS = PS + 2
    elif RunsDie[DieResult] == "3":
        print("He Runs hard for a 3")
        PS = PS + 3
    return PS


print("Welcome to the code version of pocket cricket")
print()
sleep(5)
print()
print("Let's do the toss")
while RunsDie[Run1] == RunsDie[Run2]:
    print()
    sleep(2)
    print()
    print("Rolling Dice for Player 1")
    print()
    sleep(2)
    print()
    Run1 = randint(0,5)
    print("Result of Dice for Player 1: " + RunsDie[Run1])
    print()
    sleep(2)
    print()
    print("Rolling Dice for Player 2")
    print()
    sleep(2)
    print()
    Run2 = randint(0,5)
    print("Result of Dice for Player 2: " + RunsDie[Run2])
    print()
    sleep(2)
    print()
    if RunsDie[Run1] == RunsDie[Run2]:
        print("It's a Tie! Lets do that again!")
if Run1 > Run2:
    print("Player1 Has won the toss")

    print()
    sleep(2)
    print()

    while not ChoiceValid:
        Choice = str(input("What do you choose Player 1? "))
        if Choice.upper() == "BAT":
            PlayerChoice1 = "BAT"
            PlayerChoice2 = "BOWL"
            ChoiceValid = True
        elif Choice.upper() == "BOWL" or Choice.upper() == "FIELD":
            PlayerChoice1 = "BOWL"
            PlayerChoice2 = "BAT"
            ChoiceValid = True
        else:
            print("Enter a Valid Choice") 
else:
    print("Player2 Has won the toss")
    print()
    sleep(2)
    print()
    while not ChoiceValid:
        Choice = str(input("What do you choose Player 2? "))
        if Choice.upper() == "BAT":
            PlayerChoice2 = "BAT"
            PlayerChoice1 = "BOWL"
            ChoiceValid = True
        elif Choice.upper() == "BOWL" or Choice.upper() == "FIELD":
            PlayerChoice2 = "BOWL"
            PlayerChoice1 = "BAT"
            ChoiceValid = True
        else:
            print("Enter a Valid Choice [Type 'BAT' OR ('BOWL' OR 'FIELD')]") 
print()
sleep(3)
print()
print("So Player 1 will " + PlayerChoice1.lower())
print("And Player 2 will " + PlayerChoice2.lower())
print()
sleep(2)
print()
print("Let's Play!")
print()
sleep(5)
print()
if PlayerChoice1 == "BAT":
    while not Out:
        FreeHit = False
        DieChoice = False
        AggressiveDieChoosen = False
        ConservativeDieChoosen = False
        RD = False
        UD = False
        FD = False
        PlayerBalls1 = PlayerBalls1 + 1
        print("Player 2 is now rolling the Bowling Dice")
        print()
        sleep(3)
        print()
        Bowling = randint(0, 5)
        DieChoice, Out, PlayerBalls1, PlayerScore1, NBFH = BD(Bowling, PlayerScore1, PlayerBalls1)
        print()
        sleep(3)
        print()
        if DieChoice:
            print("Bowler hasn't got the batsman out yet!")
            print()
            sleep(2)
            print()
            BatsmanDiceChoice = str(input("Does Player1 want the batsman to go Aggressive (High chances of getting out) or Conservative (Low chances of getting out)? "))
            print()
            sleep(2)
            print()
            if BatsmanDiceChoice.upper() == "AGGRESSIVE" or BatsmanDiceChoice.upper() == "A":
                print("Alright Aggresive Dice it is!")
                AggressiveDieChoosen = True
            elif BatsmanDiceChoice.upper() == "CONSERVATIVE" or BatsmanDiceChoice.upper() == "C":
                print("Alright Conservative Dice it is!")
                ConservativeDieChoosen = True
            else:
                print("Enter Valid Choice [Type ('AGGRESSIVE' OR 'A') OR ('CONSERVATIVE' OR 'C')]")
            print()
            sleep(3)
            print()
        if ConservativeDieChoosen:
            print("Player 1 is now rolling the Conservative Dice")
            print()
            sleep(3)
            print()
            Batting = randint(0,5)
            RD, UD = CD(Batting, NBFH)
            print()
            sleep(3)
            print()
        elif AggressiveDieChoosen:
            print("Player 1 is now rolling the Aggressive Dice")
            print()
            sleep(3)
            print()
            Batting = randint(0,5)
            FD, PlayerScore1 = AD(Batting, PlayerScore1, FreeHit)
            print()
            sleep(3)
            print()
        if FD:
            print("Player 2 is now rolling the Fielding Dice")
            print()
            sleep(3)
            print()
            Fielding = randint(0,5) 
            RD, Out, UD = FeD(Fielding, Batting)
            print()
            sleep(3)
            print()
        if UD:
            print("Player 2 is now rolling the Umpiring Dice")
            print()
            sleep(3)
            print()
            UmpireCall = randint(0, 5)
            RD, Out = UmD(UmpireCall, Fielding)
            print()
            sleep(3)
            print()
        if RD:
            print("Player 1 is now rolling the Run Dice")
            print()
            sleep(3)
            print()
            Run = randint(0, 5)
            PlayerScore1 = RuD(Run, PlayerScore1)
            print()
            sleep(3)
            print()

        print("Player 1 Score: " + str(PlayerScore1))
        print("Balls: " + str(PlayerBalls1))
    
    print()
    sleep(10)
    print()

    print("1st Innings is over. Player 2 needs " + str(PlayerScore1 + 1) + " Runs to win!")

    print()
    sleep(5)
    print()

    print("Let's continue!")

    Out = False
    TargetReach = False
    while not Out or not TargetReach:
        FreeHit = False
        DieChoice = False
        AggressiveDieChoosen = False
        ConservativeDieChoosen = False
        RD = False
        UD = False
        FD = False
        PlayerBalls2 = PlayerBalls2 + 1
        print("Player 1 is now rolling the Bowling Dice")
        print()
        sleep(3)
        print()
        Bowling = randint(0, 5)
        DieChoice, Out, PlayerBalls2, PlayerScore2, NBFH = BD(Bowling, PlayerScore2, PlayerBalls2)
        print()
        sleep(3)
        print()
        if DieChoice:
            print("Bowler hasn't got the batsman out yet!")
            print()
            sleep(2)
            print()
            BatsmanDiceChoice = str(input("Does Player2 want the batsman to go Aggressive (High chances of getting out) or Conservative (Low chances of getting out)? "))
            print()
            sleep(2)
            print()
            if BatsmanDiceChoice.upper() == "AGGRESSIVE" or BatsmanDiceChoice.upper() == "A":
                print("Alright Aggresive Dice it is!")
                AggressiveDieChoosen = True
            elif BatsmanDiceChoice.upper() == "CONSERVATIVE" or BatsmanDiceChoice.upper() == "C":
                print("Alright Conservative Dice it is!")
                ConservativeDieChoosen = True
            else:
                print("You have entered an Invalid Die Choice.\nIt's too late!\n No Run!\n Enter Valid Choice [Type ('AGGRESSIVE' OR 'A') OR ('CONSERVATIVE' OR 'C')]")
            print()
            sleep(3)
            print()
        if ConservativeDieChoosen:
            print("Player 2 is now rolling the Conservative Dice")
            print()
            sleep(3)
            print()
            Batting = randint(0,5)
            RD, UD = CD(Batting, NBFH)
            print()
            sleep(3)
            print()
        elif AggressiveDieChoosen:
            print("Player 2 is now rolling the Aggressive Dice")
            print()
            sleep(3)
            print()
            Batting = randint(0,5)
            FD, PlayerScore2 = AD(Batting, PlayerScore2, FreeHit)
            print()
            sleep(3)
            print()
        if FD:
            print("Player 2 is now rolling the Fielding Dice")
            print()
            sleep(3)
            print()
            Fielding = randint(0,5) 
            RD, Out, UD = FeD(Fielding, Batting)
            print()
            sleep(3)
            print()
        if UD:
            print("Player 2 is now rolling the Umpiring Dice")
            print()
            sleep(3)
            print()
            UmpireCall = randint(0, 5)
            RD, Out = UmD(UmpireCall, Fielding)
            print()
            sleep(3)
            print()
        if RD:
            print("Player 1 is now rolling the Run Dice")
            print()
            sleep(3)
            print()
            Run = randint(0, 5)
            PlayerScore2 = RuD(Run, PlayerScore2)
            print()
            sleep(3)
            print()

        print("Player 2 Score: " + str(PlayerScore2))
        print("Balls: " + str(PlayerBalls2))

        print()
        sleep(3)
        print()

        if PlayerScore1 > PlayerScore2:
            print("Player2 Needs " + str(((PlayerScore1 + 1) - PlayerScore2)) + " More Run(s) to win!")
            TargetReach = True
        elif PlayerScore1 == PlayerScore2:
            print("Scores Are tied!")
        else:
            TargetReach = True

    print()
    sleep(5)
    print()

    print("Match Over!")
    if PlayerScore1 > PlayerScore2:
        print("Player1 Won the Match")
    elif PlayerScore1 == PlayerScore2:
        print("Scores Are tied!")
    else:
        print("Player2 Won the Match")
elif PlayerChoice2 == "BAT":
    while not Out:
        FreeHit = False
        DieChoice = False
        AggressiveDieChoosen = False
        ConservativeDieChoosen = False
        RD = False
        UD = False
        FD = False
        PlayerBalls2 = PlayerBalls2 + 1
        print("Player 1 is now rolling the Bowling Dice")
        print()
        sleep(3)
        print()
        Bowling = randint(0, 5)
        DieChoice, Out, PlayerBalls2, PlayerScore2, NBFH = BD(Bowling, PlayerScore2, PlayerBalls2)
        print()
        sleep(3)
        print()
        if DieChoice:
            print("Bowler hasn't got the batsman out yet!")
            print()
            sleep(2)
            print()
            BatsmanDiceChoice = str(input("Does Player2 want the batsman to go Aggressive (High chances of getting out) or Conservative (Low chances of getting out)? "))
            print()
            sleep(2)
            print()
            if BatsmanDiceChoice.upper() == "AGGRESSIVE" or BatsmanDiceChoice.upper() == "A":
                print("Alright Aggresive Dice it is!")
                AggressiveDieChoosen = True
            elif BatsmanDiceChoice.upper() == "CONSERVATIVE" or BatsmanDiceChoice.upper() == "C":
                print("Alright Conservative Dice it is!")
                ConservativeDieChoosen = True
            else:
                print("You have entered an Invalid Die Choice.\nIt's too late!\n No Run!\n Enter Valid Choice [Type ('AGGRESSIVE' OR 'A') OR ('CONSERVATIVE' OR 'C')]")
            print()
            sleep(3)
            print()
        if ConservativeDieChoosen:
            print("Player 2 is now rolling the Conservative Dice")
            print()
            sleep(3)
            print()
            Batting = randint(0,5)
            RD, UD = CD(Batting, NBFH)
            print()
            sleep(3)
            print()
        elif AggressiveDieChoosen:
            print("Player 2 is now rolling the Aggressive Dice")
            print()
            sleep(3)
            print()
            Batting = randint(0,5)
            FD, PlayerScore2 = AD(Batting, PlayerScore2, FreeHit)
            print()
            sleep(3)
            print()
        if FD:
            print("Player 1 is now rolling the Fielding Dice")
            print()
            sleep(3)
            print()
            Fielding = randint(0,5) 
            RD, Out, UD = FeD(Fielding, Batting)
            print()
            sleep(3)
            print()
        if UD:
            print("Player 1 is now rolling the Umpiring Dice")
            print()
            sleep(3)
            print()
            UmpireCall = randint(0, 5)
            RD, Out = UmD(UmpireCall, Fielding)
            print()
            sleep(3)
            print()
        if RD:
            print("Player 2 is now rolling the Run Dice")
            print()
            sleep(3)
            print()
            Run = randint(0, 5)
            PlayerScore2 = RuD(Run, PlayerScore2)
            print()
            sleep(3)
            print()

        print("Player 2 Score: " + str(PlayerScore2))
        print("Balls: " + str(PlayerBalls2))
    
    print()
    sleep(10)
    print()

    print("1st Innings is over. Player 1 needs " + str(PlayerScore2 + 1) + " Runs to win!")

    print()
    sleep(5)
    print()

    print("Let's continue!")

    Out = False
    TargetReach = False
    while not Out or not TargetReach:
        FreeHit = False
        DieChoice = False
        AggressiveDieChoosen = False
        ConservativeDieChoosen = False
        RD = False
        UD = False
        FD = False
        PlayerBalls1 = PlayerBalls1 + 1
        print("Player 2 is now rolling the Bowling Dice")
        print()
        sleep(3)
        print()
        Bowling = randint(0, 5)
        DieChoice, Out, PlayerBalls1, PlayerScore1, NBFH = BD(Bowling, PlayerScore1, PlayerBalls1)
        print()
        sleep(3)
        print()
        if DieChoice:
            print("Bowler hasn't got the batsman out yet!")
            print()
            sleep(2)
            print()
            BatsmanDiceChoice = str(input("Does Player1 want the batsman to go Aggressive (High chances of getting out) or Conservative (Low chances of getting out)? "))
            print()
            sleep(2)
            print()
            if BatsmanDiceChoice.upper() == "AGGRESSIVE" or BatsmanDiceChoice.upper() == "A":
                print("Alright Aggresive Dice it is!")
                AggressiveDieChoosen = True
            elif BatsmanDiceChoice.upper() == "CONSERVATIVE" or BatsmanDiceChoice.upper() == "C":
                print("Alright Conservative Dice it is!")
                ConservativeDieChoosen = True
            else:
                print("You have entered an Invalid Die Choice.\nIt's too late!\n No Run!\n Enter Valid Choice [Type ('AGGRESSIVE' OR 'A') OR ('CONSERVATIVE' OR 'C')]")
            print()
            sleep(3)
            print()
        if ConservativeDieChoosen:
            print("Player 1 is now rolling the Conservative Dice")
            print()
            sleep(3)
            print()
            Batting = randint(0,5)
            RD, UD = CD(Batting, NBFH)
            print()
            sleep(3)
            print()
        elif AggressiveDieChoosen:
            print("Player 1 is now rolling the Aggressive Dice")
            print()
            sleep(3)
            print()
            Batting = randint(0,5)
            FD, PlayerScore1 = AD(Batting, PlayerScore1, FreeHit)
            print()
            sleep(3)
            print()
        if FD:
            print("Player 2 is now rolling the Fielding Dice")
            print()
            sleep(3)
            print()
            Fielding = randint(0,5) 
            RD, Out, UD = FeD(Fielding, Batting)
            print()
            sleep(3)
            print()
        if UD:
            print("Player 2 is now rolling the Umpiring Dice")
            print()
            sleep(3)
            print()
            UmpireCall = randint(0, 5)
            RD, Out = UmD(UmpireCall, Fielding)
            print()
            sleep(3)
            print()
        if RD:
            print("Player 1 is now rolling the Run Dice")
            print()
            sleep(3)
            print()
            Run = randint(0, 5)
            PlayerScore1 = RuD(Run, PlayerScore1)
            print()
            sleep(3)
            print()

        print("Player 1 Score: " + str(PlayerScore1))
        print("Balls: " + str(PlayerBalls1))

        print()
        sleep(3)
        print()

        if PlayerScore2 > PlayerScore1:
            print("Player1 Needs " + str(((PlayerScore2 + 1) - PlayerScore1)) + " More Run(s) to win!")
            TargetReach = True
        elif PlayerScore1 == PlayerScore2:
            print("Scores Are tied!")
        else:
            TargetReach = True

    print()
    sleep(5)
    print()

    print("Match Over!")
    if PlayerScore2 > PlayerScore1:
        print("Player1 Won the Match")
    elif PlayerScore2 == PlayerScore1:
        print("Scores Are tied!")
    else:
        print("Player2 Won the Match")