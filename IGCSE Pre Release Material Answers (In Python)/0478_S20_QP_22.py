DaysShort = ["sun", "mon", "tue", "wen", "thu", "fri", "sat"]
DaysLong = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "Saturday"]
WeekDayShort = ["mon", "tue", "wen", "thu", "fri"]
WeekDayLong = ["monday", "tuesday", "wednesday", "thursday", "friday"]
Sunday = ["sun", "sunday"]
Monday = ["mon", "monday"]
Tuesday = ["tue", "tuesday"]
Wednesday = ["wed", "wednesday"]
Thursday = ["thu", "thursday"]
Friday = ["fri", "friday"]
Saturday = ["sat", "saturday"]
Yes = ["yes", "ya", "y"]
No = ["no", "nah", "n"]
MaxHourArr = [8, 2, 2, 2, 2, 2, 4]
CostPerHourArr = [2.00, 10.00, 10.00, 10.00, 10.00, 10.00, 3.00]
EveningCost = 2.00
end_day = False
DailyTotal = 0
while not end_day:
    DC1 = False
    DC2 = False
    FPNCache = []
    Correct0 = False
    while not Correct0:
        try:
            print("")
            D = str(input("Enter Day: "))
            Day = D.lower()
            if Day in DaysShort or Day in DaysLong:
                Correct0 = True
            else:
                print("Enter valid day")
        except ValueError:
            print("Enter valid value")
    print("Enter in Hours Only (Example: if the time is 15:45, then input 15. Parking allowed from 0800 to 0000. NO PARKING IS ALLOWED FROM 0001 to 0759")
    Correct1 = False
    while not Correct1:
        try:
            print("")
            TimeEntered = int(input("Enter the time you are entering: "))
            if 8 <= TimeEntered < 24:
                Correct1 = True
            else:
                print("Enter Valid Time in Hours only")
        except ValueError:
            print("Enter Valid Value")
    if Day in DaysShort:
        Loc = DaysShort.index(Day)
    elif Day in DaysLong:
        Loc = DaysLong.index(Day)
    if TimeEntered >= 16:
        MaxHour = 24 - TimeEntered
        CostPerHour = EveningCost
        EstimatedTime = TimeEntered + MaxHour
    else:
        if Day in WeekDayShort or Day in WeekDayLong:
            MaxHour = MaxHourArr[Loc]
            CostPerHour = CostPerHourArr[Loc]
            EstimatedTime = TimeEntered + MaxHour
        elif Day in Saturday:
            MaxHour = MaxHourArr[Loc]
            CostPerHour = CostPerHourArr[Loc]
            EstimatedTime = TimeEntered + MaxHour
        else:
            MaxHour = MaxHourArr[Loc]
            CostPerHour = CostPerHourArr[Loc]
            EstimatedTime = TimeEntered + MaxHour
    print("Cost Per Hour: $" + str(CostPerHour))
    if EstimatedTime >= 16 > TimeEntered:
        MaxHour = 24 - TimeEntered
        print("You can stay until Midnight")
        print("Evening Cost (Flat Fare): $" + str(EveningCost))
        print("Maximum Hours: " + str(MaxHour))
    else:
        print("Maximum Hours: " + str(MaxHour))
    Correct2 = False
    while not Correct2:
        try:
            print("")
            TimeExit = int(input("How many hours do you want to leave your car for: "))
            if MaxHour >= TimeExit > 0:
                Correct2 = True
            else:
                print("Enter Valid Time")
        except ValueError:
            print("Enter Valid Value")
    CustomerTotal = 0
    DepartureTime = TimeEntered + TimeExit
    if DepartureTime > 16 >= TimeEntered:
        TimeMorning = 16 - TimeEntered
        TimeCostMorning = float(TimeMorning * CostPerHour)
        TimeCostEvening = float(EveningCost)
        CustomerTotal = float(TimeCostMorning + TimeCostEvening)
        print("Time has exceeded the evening timing prices.")
    elif TimeEntered >= 16:
        CustomerTotal = EveningCost
    else:
        CustomerTotal = TimeExit * CostPerHour
    print("Your Total: $" + str(CustomerTotal))
    Correct3 = False
    print("")
    while not Correct3:
        try:
            print("")
            Ch = str(input("Do you want to try entering the frequent parking number: "))
            Choice = Ch.lower()
            if Choice in Yes or Choice in No:
                Correct3 = True
            else:
                print("Enter Valid Value")
        except ValueError:
            print("Enter Valid Value")
    if Choice in Yes:
        print("")
        print("Alright. You only have one chance to enter the 5 digit Frequent Parking Number.")
        if TimeEntered >= 16:
            print("50% Discount available if you answer this right")
        else:
            print("10% Discount available if you answer this right")
        Correct4 = False
        print("")
        while not Correct4:
            try:
                print("")
                FPN = int(input("Now enter the frequent parking number: "))
                if 10000 <= FPN < 100000:
                    Correct4 = True
                else:
                    print("Enter 5 digit Frequent Parking Number")
            except ValueError:
                print("Enter Valid Value")
        while FPN > 0:
            Y = FPN % 10
            FPNCache.insert(0, Y)
            FPN = int(FPN / 10)
        D1 = FPNCache[0] * 5
        D2 = FPNCache[1] * 4
        D3 = FPNCache[2] * 3
        D4 = FPNCache[3] * 2
        D5 = FPNCache[4]
        Sum = D1 + D2 + D3 + D4
        Reminder = int(Sum % 11)
        Checker = 11 - Reminder
        if Checker == D5:
            print("")
            print("Good Job. You have entered the correct Parking Number.")
            print("")
            if TimeEntered >= 16:
                print("You have received a 50% Discount")
                DC1 = True
            else:
                print("You have received a 10% Discount")
                DC2 = True
        else:
            print("Sorry. You have entered the wrong Parking Number.")
    else:
        print("Ok. You have no Discounts")
    if DC1:
        GT = float(CustomerTotal * 0.5)
        GrandTotal = round(GT, 2)
    elif DC2:
        GT = float(CustomerTotal * 0.9)
        GrandTotal = round(GT, 2)
    else:
        GT = float(CustomerTotal)
        GrandTotal = round(GT, 2)
    print("Your Grand Total: $" + str(GrandTotal))
    Correct5 = False
    while not Correct5:
        try:
            print("")
            GrandTotalPaid = float(input("Enter the amount you want to Pay.\nThe amount Must be Greater Than OR Equal to the amount you want to pay.\nNO Change will be given.\nEnter Value: "))
            if GrandTotalPaid >= GrandTotal:
                Correct6 = False
                while not Correct6:
                    try:
                        print("")
                        S = str(input("Are you sure you want to pay the amount " + str(GrandTotalPaid) + "?: "))
                        Sure = S.lower()
                        if Sure in Yes or Sure in No:
                            Correct6 = True
                        else:
                            print("Enter Valid Choice")
                    except ValueError:
                        print("Enter Valid Value")
                if Sure in Yes:
                    print("Ok amount has been paid.")
                    DailyTotal = DailyTotal + GrandTotalPaid
                    Correct5 = True
                else:
                    print("Ok Enter Again")
            else:
                print("Enter Greater Value")
        except ValueError:
            print("Enter Valid Value")
    print("Thank You for your Co-operation. Have a Nice Day!!")
    Correct7 = False
    while not Correct7:
        try:
            ED = str(input("Do you want to end the day?: "))
            End = ED.lower()
            if End in Yes or End in No:
                Correct7 = True
            else:
                print ("Enter Valid Choice")
        except ValueError:
            print("Enter Valid Value")
    if End in Yes:
        Correct8 = False
        while not Correct8:
            try:
                Password = int(input("Enter 4 digit Password to end the day: "))
                if 999 < Password < 10000:
                    if Password == 1234:
                        print("Day has ended.")
                        print("Daily Total: " + str(DailyTotal))
                        Correct8 = True
                        end_day = True
                    else:
                        Correct9 = False
                        while not Correct9:
                            try:
                                Ag = str(input("Wrong password entered. Do you want to try again?: "))
                                Again = Ag.lower()
                                if Again in Yes or Again in No:
                                    Correct9 = True
                                else:
                                    print("Enter Valid Choice")
                            except ValueError:
                                print("Enter Valid Value")
                        if Again in Yes:
                            print("Ok enter again")
                        else:
                            print("Ok Continuing with day")
                            Correct8 = True
                else:
                    print("Enter 4 digit Password")
            except ValueError:
                print("Enter Valid Value")
    else:
        print("Ok. Continuing with the day.")