BTH = []
BTN = []
BTA = []
P = []
H = 3
T = 10
M = (H * 60) / T
R = int(M)

for i in range(R):
    print("")
    BT = float(input("Enter baby Temperature: "))
    BTH.append(BT)
    if 36.0 <= BT <= 37.0:
        print("Baby Temperature is normal")
        Normal = "True"
        High = "Normal"
        BTN.append(Normal)
        BTA.append(High)
    else:
        print("Baby Temperature is Abnormal")
        Normal = "False"
        BTN.append(Normal)
        if 37.0 < BT:
            print("Baby temperature is too high")
            High = "True"
            BTA.append(High)
        elif 36.0 > BT:
            print("Baby temperature is too low")
            High = "False"
            BTA.append(High)

BTH.sort()
LT = BTH[0]
LTStr = str(LT)
BTH.sort(reverse=True)
HT = BTH[0]
HTStr = str(HT)
TD = HT - LT
TDStr = str(TD)
print("")
print("Lowest Temperature of Baby: " + LTStr)
print("Highest Temperature of Baby: " + HTStr)
print("Difference in Temperature of Baby: " + TDStr)

for i in range(R):
    X = BTN.count("False")
    if X >= 2:
        if BTA[i] == "True":
            Checker1 = BTA.count("True")
            C1str = str(Checker1)
            Problem = "The Temperature went too high " + C1str + " times"
            P.append(Problem)
        elif BTA[i] == "False":
            Checker1 = BTA.count("False")
            C1str = str(Checker1)
            Problem = "The Temperature went too low " + C1str + " times"
            P.append(Problem)

    if TD > 1:
        Problem = "The Temperature difference is more than 1 degree celsius"
        P.append(Problem)

if len(P) > 0:
    S = list(set(P))
    for i in S:
        print("")
        print(i)
else:
    print("No problems have occurred")
