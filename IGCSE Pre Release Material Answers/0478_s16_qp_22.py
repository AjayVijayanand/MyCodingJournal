Content = ["C", "G", "S"]
Yes = ["yes", "y", "ya"]
No = ["no", "n", "nah"]
YN = ["no", "n", "nah", "yes", "y", "ya"]
Accepted = 0
Rejected = 0
AcceptedContent = []
AcceptedWeight = []
Start_Day = False
Correct0 = False
while not Start_Day:
    while not Correct0:
        try:
            print("What Sacks do you want?")
            print("C - Cement")
            print("G - Gravel")
            print("S - Sand")
            Choice = str(input("Enter Sack Content: "))
            SackChoice = Choice.upper()
            if SackChoice in Content:
                Correct0 = True
            else:
                print("Enter Valid Value")
        except ValueError:
            print("Enter Valid Value")
    Correct1 = False
    SG = False
    C = False
    while not Correct1:
        try:
            print("Enter Weight of Sack")
            if SackChoice == "S" or SackChoice == "G":
                print("Sand or Gravel must weigh over 49.9 and under 50.1 kilograms")
                SG = True
            else:
                print("Cement must weigh over 24.9 and under 25.1 kilograms")
                C = True
            Weight = float(input("Enter Weight: "))
            if Weight > 0:
                Correct1 = True
            else:
                print("Enter Valid Value")
        except ValueError:
            print("Enter Valid Value")

    if SG:
        if 49.9 < Weight < 50.1:
            print("Accepted!!")
            Accepted = Accepted + 1
        else:
            print("Rejected")
            Rejected = Rejected + 1

    elif C:
        if 24.9 < Weight < 25.1:
            print("Accepted!!")
            Accepted = Accepted + 1
            AcceptedContent.append(SackChoice)
            AcceptedWeight.append(Weight)
        else:
            print("Rejected")
            Rejected = Rejected + 1
            AcceptedContent.append("Rejected")
            AcceptedWeight.append("Rejected")
    Correct2 = False
    while not Correct2:
        try:
            Start = str(input("Enter Sack Content: "))
            Day = Start.lower()
            if Day in YN:
                Correct2 = True
            else:
                print("Enter Valid Value")
        except ValueError:
            print("Enter Valid Value")
    if Day in Yes:
        print("Time to Start the Day")
        Start_Day = True
    elif Day in No:
        print("Ok. Continue...")

