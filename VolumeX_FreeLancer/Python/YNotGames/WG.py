from random import randint

with open("VolumeX_FreeLancer\Python\YNotGames\hrt.txt", "r") as w:
    WordList = w.readlines()

Word = WordList[randint(0, len(WordList))]
Word = Word.upper()
Letters = list(Word)
Count = len(Word) - 1
Tries = 0
RLetters = GLetters = [''] * (Count + 1)
print("This word has " + str(Count) + " Letters.")
for x in range(Count + 1):
    Tries = Count - x
    Valid = False
    while not Valid:
        try:
            GW = str(input("Enter Guess: "))
            GW = GW + " "
            if len(GW) == Count + 1:
                Valid = True
            else:
                print("Enter " + str(Count) + " Letter Word")
        except:
            print("Enter Valid Value!")
    GWord = GW.upper()
    GLetters = list(GWord)
    Guessed = True
    for x in range(len(Word) - 1):
        if GLetters[x] == Letters[x]:
            RLetters[x] = Letters[x]
        else:
            Guessed = False
            RLetters[x] = "*"
    if Guessed:
        print("Congratulations you have guessed the word!")
        break
    else:
        print("You have not guessed the word!")
        print(' '.join(RLetters))
        WronglyPlaced = []
        for y in Letters:
            for z in GLetters:
                if y == z and y not in RLetters and y not in WronglyPlaced:
                    WronglyPlaced.append(y)
        print("Some Letters that are wrongly placed: " + str(WronglyPlaced))
        print("Tries Left " + str(Tries))

if not Guessed:
    print("You have completed all tries!")
    print("But unfortunately you have not guessed the correct word :(")
if Guessed:
    print("It took you " + str(x) + " Guesses")
print("The Correct word is: " + Word)