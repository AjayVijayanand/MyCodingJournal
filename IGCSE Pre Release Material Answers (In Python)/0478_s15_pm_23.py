MDT = []
MNT = []

for i in range(30):
    r = i + 1
    s = str(r)
    print()
    print("Enter Temperatures for Day: " + s)
    DT = float(input("Enter Midday Temperature: "))
    MDT.append(DT)
    DTS = str(DT)
    NT = float(input("Enter Midnight Temperature: "))
    MNT.append(NT)
    NTS = str(NT)

TDT = sum(MDT)
TNT = sum(MNT)
EDT = len(MDT)
ENT = len(MNT)
MDTAvg = TDT / EDT
MNTAvg = TNT / ENT
MDTAvgStr = str(MDTAvg)
MNTAvgStr = str(MNTAvg)

print("Average Midday: " + MDTAvgStr)
print("Average Midnight: " + MNTAvgStr)

MDT.sort(reverse=True)
MNT.sort()
HTD = MDT[0]
LTN = MNT[0]
HTDStr = str(HTD)
LTNStr = str(LTN)
print("Highest Temperature Midday: " + HTDStr)
print("Lowest Temperature Midnight: " + LTNStr)
