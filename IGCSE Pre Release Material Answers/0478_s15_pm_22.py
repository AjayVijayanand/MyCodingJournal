Stud_Name = []
Stud_Weight_Start = []
Stud_Weight_End = []
Stud_Weight_Diff = []
Stud_Increase = []
Stud_Check = []

R = int(input("Enter Number Of Students: "))
for i in range(R):
    S = str(input("Enter Student Name: "))
    Stud_Name.append(S)
    SS = float(input("Enter Student Weight in the start of the term: "))
    SWS = str(SS)
    Stud_Weight_Start.append(SWS)
    SE = float(input("Enter Student Weight in the end of the term: "))
    SWE = str(SE)
    Stud_Weight_End.append(SWE)
    SD = SE - SS
    SWD = str(SD)
    Stud_Weight_Diff.append(SWD)
    if 2.5 < SD or -2.5 > SD:
        Checker2 = True
        Stud_Check.append(Checker2)
        if SD < 0:
            Checker = False
            Stud_Increase.append(Checker)
        elif SD > 0:
            Checker = True
            Stud_Increase.append(Checker)
    else:
        Checker2 = False
        if SD < 0:
            Checker = False
            Stud_Increase.append(Checker)
        elif SD > 0:
            Checker = True
            Stud_Increase.append(Checker)
        Stud_Check.append(Checker2)

for i in range(R):
    print("\nName: " + Stud_Name[i])
    print("Weight(Start of Term): " + Stud_Weight_Start[i])
    print("Weight(End of term): " + Stud_Weight_End[i])
    print("Weight Difference: " + Stud_Weight_Diff[i])
    if Stud_Check[i]:
        if Stud_Increase[i]:
            print("Student weight has increased")
        else:
            print("Student weight has decreased")
    else:
        if Stud_Increase[i]:
            print("Student Weight has increased by less than +2.5")
        else:
            print("Student Weight has decreased by more than -2.5")