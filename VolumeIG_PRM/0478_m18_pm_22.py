Subjects = ["physics", "chemistry", "history", "geography", "computer science"]
Physics = 0
Chemistry = 0
History = 0
Geography = 0
ComputerSci = 0
StudentName = []
ChosenSubject1 = []
ChosenSubject2 = []
SubjectReject = []

Correct0 = False
while not Correct0:
    try:
        StudentRoll = int(input("Enter number of students: "))
        if StudentRoll > 0:
            Correct0 = True
        else:
            print("Enter Valid Value")
    except ValueError:
        print("Enter Valid Value")

for Roll in range(StudentRoll):
    Correct1 = False
    while not Correct1:
        try:
            SN = str(input("Enter name of student: "))
            if not ValueError:
                Correct1 = True
        except ValueError:
            print("Enter Valid Value")
    available1 = False
    while not available1:
        Correct2 = False
        while not Correct2:
            try:
                Sub1 = str(input("Enter Subject Choice 1: "))
                SubjectChoice1 = Sub1.lower()
                if SubjectChoice1 in Subjects:
                    Correct2 = True
                else:
                    print("Enter Valid Value")
            except ValueError:
                print("Enter Valid Value")
        if SubjectChoice1 == "physics":
            if Physics < 40:
                print("Subject Choice Available")
                Physics = Physics + 1
                print("Number of Students in Physics: " + str(Physics))
                available1 = True
            else:
                print("Subject is full")
                print("Available Subjects:")
                if Chemistry < 40:
                    print("Chemistry")
                    print("Available Slots: " + str(40 - Chemistry))
                if History < 40:
                    print("History")
                    print("Available Slots: " + str(40 - History))
                if Geography < 40:
                    print("Geography")
                    print("Available Slots: " + str(40 - Geography))
                if ComputerSci < 40:
                    print("Computer Science")
                    print("Available Slots: " + str(40 - ComputerSci))
                else:
                    print("None")

        if SubjectChoice1 == "chemistry":
            if Chemistry < 40:
                print("Subject Choice Available")
                Chemistry = Chemistry + 1
                print("Number of Students in Chemistry: " + str(Chemistry))
                available1 = True
            else:
                print("Subject is full")
                print("Available Subjects:")
                if Physics < 40:
                    print("Physics")
                    print("Available Slots: " + str(40 - Physics))
                if History < 40:
                    print("History")
                    print("Available Slots: " + str(40 - History))
                if Geography < 40:
                    print("Geography")
                    print("Available Slots: " + str(40 - Geography))
                if ComputerSci < 40:
                    print("Computer Science")
                    print("Available Slots: " + str(40 - ComputerSci))
                else:
                    print("None")

        if SubjectChoice1 == "history":
            if History < 40:
                print("Subject Choice Available")
                History = History + 1
                print("Number of Students in History: " + str(History))
                available1 = True
            else:
                print("Subject is full")
                print("Available Subjects:")
                if Physics < 40:
                    print("Physics")
                    print("Available Slots: " + str(40 - Physics))
                if Chemistry < 40:
                    print("Chemistry")
                    print("Available Slots: " + str(40 - Chemistry))
                if Geography < 40:
                    print("Geography")
                    print("Available Slots: " + str(40 - Geography))
                if ComputerSci < 40:
                    print("Computer Science")
                    print("Available Slots: " + str(40 - ComputerSci))
                else:
                    print("None")

        if SubjectChoice1 == "geography":
            if Geography < 40:
                print("Subject Choice Available")
                Geography = Geography + 1
                print("Number of Students in Geography: " + str(Geography))
                available1 = True
            else:
                print("Subject is full")
                print("Available Subjects:")
                if Physics < 40:
                    print("Physics")
                    print("Available Slots: " + str(40 - Physics))
                if Chemistry < 40:
                    print("Chemistry")
                    print("Available Slots: " + str(40 - Chemistry))
                if History < 40:
                    print("History")
                    print("Available Slots: " + str(40 - History))
                if ComputerSci < 40:
                    print("Computer Science")
                    print("Available Slots: " + str(40 - ComputerSci))
                else:
                    print("None")

        if SubjectChoice1 == "computer science":
            if ComputerSci < 40:
                print("Subject Choice Available")
                ComputerSci = ComputerSci + 1
                print("Number of Students in Computer Science: " + str(ComputerSci))
                available1 = True
            else:
                print("Subject is full")
                print("Available Subjects:")
                if Physics < 40:
                    print("Physics")
                    print("Available Slots: " + str(40 - Physics))
                if Chemistry < 40:
                    print("Chemistry")
                    print("Available Slots: " + str(40 - Chemistry))
                if History < 40:
                    print("History")
                    print("Available Slots: " + str(40 - History))
                if Geography < 40:
                    print("Geography")
                    print("Available Slots: " + str(40 - Geography))
                else:
                    print("None")

    available2 = False
    while not available2:
        Correct3 = False
        while not Correct3:
            try:
                Sub2 = str(input("Enter Subject Choice 1: "))
                SubjectChoice2 = Sub2.lower()
                if SubjectChoice2 in Subjects:
                    Correct2 = True
                else:
                    print("Enter Valid Value")
            except ValueError:
                print("Enter Valid Value")
        if SubjectChoice2 == "physics" and SubjectChoice1 != "physics":
            if Physics < 40:
                print("Subject Choice Available")
                Physics = Physics + 1
                print("Number of Students in Physics: " + str(Physics))
                available2 = True
            else:
                if Physics >= 40:
                    print("Subject is full")
                elif SubjectChoice1 == "physics":
                    print("Subject already chosen")
                print("Available Subjects:")
                if Chemistry < 40 and SubjectChoice1 != "chemistry":
                    print("Chemistry")
                    print("Available Slots: " + str(40 - Chemistry))
                if History < 40 and SubjectChoice1 != "history":
                    print("History")
                    print("Available Slots: " + str(40 - History))
                if Geography < 40 and SubjectChoice1 != "geography":
                    print("Geography")
                    print("Available Slots: " + str(40 - Geography))
                if ComputerSci < 40 and SubjectChoice1 != "computer science":
                    print("Computer Science")
                    print("Available Slots: " + str(40 - ComputerSci))
                else:
                    print("None")

        if SubjectChoice2 == "chemistry" and SubjectChoice1 != "chemistry":
            if Chemistry < 40:
                print("Subject Choice Available")
                Chemistry = Chemistry + 1
                print("Number of Students in Chemistry: " + str(Chemistry))
                available2 = True
            else:
                if Chemistry >= 40:
                    print("Subject is full")
                elif SubjectChoice1 == "chemistry":
                    print("Subject already chosen")
                print("Available Subjects:")
                if Physics < 40 and SubjectChoice1 != "physics":
                    print("Physics")
                    print("Available Slots: " + str(40 - Physics))
                if History < 40 and SubjectChoice1 != "history":
                    print("History")
                    print("Available Slots: " + str(40 - History))
                if Geography < 40 and SubjectChoice1 != "geography":
                    print("Geography")
                    print("Available Slots: " + str(40 - Geography))
                if ComputerSci < 40 and SubjectChoice1 != "computer science":
                    print("Computer Science")
                    print("Available Slots: " + str(40 - ComputerSci))
                else:
                    print("None")

        if SubjectChoice2 == "history" and SubjectChoice1 != "history":
            if History < 40:
                print("Subject Choice Available")
                History = History + 1
                print("Number of Students in History: " + str(History))
                available2 = True
            else:
                if History >= 40:
                    print("Subject is full")
                elif SubjectChoice1 == "history":
                    print("Subject already chosen")
                print("Available Subjects:")
                if Physics < 40 and SubjectChoice1 != "physics":
                    print("Physics")
                    print("Available Slots: " + str(40 - Physics))
                if Chemistry < 40 and SubjectChoice1 != "chemistry":
                    print("Chemistry")
                    print("Available Slots: " + str(40 - Chemistry))
                if Geography < 40 and SubjectChoice1 != "geography":
                    print("Geography")
                    print("Available Slots: " + str(40 - Geography))
                if ComputerSci < 40 and SubjectChoice1 != "computer science":
                    print("Computer Science")
                    print("Available Slots: " + str(40 - ComputerSci))
                else:
                    print("None")

        if SubjectChoice2 == "geography" and SubjectChoice1 != "geography":
            if Geography < 40:
                print("Subject Choice Available")
                Geography = Geography + 1
                print("Number of Students in Geography: " + str(Geography))
                available1 = True
            else:
                print("Subject is full")
                print("Available Subjects:")
                if Physics < 40 and SubjectChoice1 != "physics":
                    print("Physics")
                    print("Available Slots: " + str(40 - Physics))
                if Chemistry < 40 and SubjectChoice1 != "chemistry":
                    print("Chemistry")
                    print("Available Slots: " + str(40 - Chemistry))
                if History < 40 and SubjectChoice1 != "history":
                    print("History")
                    print("Available Slots: " + str(40 - History))
                if ComputerSci < 40 and SubjectChoice1 != "computer science":
                    print("Computer Science")
                    print("Available Slots: " + str(40 - ComputerSci))
                else:
                    print("None")

        if SubjectChoice2 == "computer science" and SubjectChoice1 != "computer science":
            if ComputerSci < 40:
                print("Subject Choice Available")
                ComputerSci = ComputerSci + 1
                print("Number of Students in Computer Science: " + str(ComputerSci))
                available1 = True
            else:
                print("Subject is full")
                print("Available Subjects:")
                if Physics < 40 and SubjectChoice1 != "physics":
                    print("Physics")
                    print("Available Slots: " + str(40 - Physics))
                if Chemistry < 40 and SubjectChoice1 != "chemistry":
                    print("Chemistry")
                    print("Available Slots: " + str(40 - Chemistry))
                if History < 40 and SubjectChoice1 != "history":
                    print("History")
                    print("Available Slots: " + str(40 - History))
                if Geography < 40 and SubjectChoice1 != "geography":
                    print("Geography")
                    print("Available Slots: " + str(40 - Geography))
                else:
                    print("None")

print("Number of Students in Physics: " + str(Physics))
print("Number of Students in Chemistry: " + str(Chemistry))
print("Number of Students in History: " + str(History))
print("Number of Students in Geography: " + str(Geography))
print("Number of Students in Computer Science: " + str(ComputerSci))