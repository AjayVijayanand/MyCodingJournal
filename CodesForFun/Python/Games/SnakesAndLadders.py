from random import *
from time import sleep

class Player:
    def __init__(self, Name, Pos):
        self.Name = Name
        self.Pos = Pos

    def movePos(self):
        ladderClimb =    [1, 4, 9, 21, 28, 36, 51, 71, 80]
        ladderClimbRes = [38, 14, 31, 42, 84, 44, 67, 91, 100]
        snakeBit =       [16, 47, 49, 56, 62, 64, 87, 93, 95, 98]
        snakeBitRes =    [6, 26, 11, 53, 19, 60, 24, 73, 75, 78]
        DiceVal = randint(1, 6)
        print(self.Name + "'s Turn")
        sleep(1)
        print (self.Name + " has rolled a " + str(DiceVal))
        sleep(1)
        self.Pos = self.Pos + DiceVal
        if self.Pos > 100:
            print (self.Name + " must roll a " + str(6 - self.Pos - 100) + " to win!") 
            self.Pos = self.Pos - DiceVal
            sleep(1)
        print (self.Name + "'s Position now: " + str(self.Pos))
        if self.Pos in ladderClimb:
            sleep(1)
            print("Congratulations " + self.Name + "! You have climbed a ladder!")
            self.Pos = ladderClimbRes[ladderClimb.index(self.Pos)]
            sleep(1)
            print (self.Name + "'s new Position is: " + str(self.Pos))
        if self.Pos in snakeBit:
            sleep(1)
            print("Oh no " + self.Name + "! You have been bitten by a snake!")
            self.Pos = snakeBitRes[snakeBit.index(self.Pos)]
            sleep(1)
            print (self.Name + "'s new Position is: " + str(self.Pos))
        if self.Pos == 100:
            sleep(2)
            print (self.Name + " Has won!")
        sleep(1)
        print()
        sleep(1)
        
print("Snakes and Ladders")
sleep(3)
namePlayer1 = str(input("Enter Name of Player 1: "))
namePlayer2 = str(input("Enter Name of Player 2: "))
sleep(3)
print(namePlayer1 + " vs " + namePlayer2)
sleep(1)
Player1 = Player(namePlayer1, 0)
Player2 = Player(namePlayer2, 0)

while True:
    Player1.movePos()
    if Player1.Pos == 100:
        break
    Player2.movePos()
    if Player2.Pos == 100:
        break