from random import randint

with open("words.txt", "r") as w:
    WordList = w.readlines()

while len(Word) != 5:
    Word = WordList[randint(len(WordList))]
Letters = list(Word)
RLetters = ['', '', '', '', '']
GLetters = ['', '', '', '', '']
Count = 5
Tries = 0
for x in range(Count):
    Tries = Count - x
    Valid = False
    while not Valid:
        try:
            GW = str(input("Enter Guess: "))
            if len(GW) == 5:
                Valid = True
            else:
                print("Enter 5 Letter Word")
        except:
            print("Enter Valid Value!")
    GWord = GW.upper()
    GLetters = list(GWord)
    Guessed = True
    for x in range(len(Word)):
        if GLetters[x] == Letters[x]:
            RLetters[x] = GLetters[x]
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
                if y == z and y not in RLetters:
                    WronglyPlaced.append(y)
        print("Some Letters that are wrongly placed: " + str(WronglyPlaced))
        print("Tries Left " + str(Tries))

if not Guessed:
    print("You have completed all tries!")
    print("But unfortunately you have not guessed the correct word :(")

print("The Correct word is: " + Word)