ATH = []
ATA = []
ATC = []
ATM = []
P = []
H = 1
T = 10
M = (H * 60) / T
R = int(M)

for i in range(R):
    print("")
    AT = float(input("Enter Apartment Temperature: "))
    ATH.append(AT)
    if 22.0 <= AT <= 24.0:
        print("Apartment Temperature is normal")
        High = "Normal"
        CO = False
        ATA.append(High)
        ATC.append(CO)
        ATM.append(CO)
    else:
        if 24.0 < AT:
            print("Apartment temperature is too high")
            High = "True"
            ATA.append(High)
            if 24.5 < AT:
                print("Cooling is on")
                CO = "True"
                ATC.append(CO)
                CO2 = "False"
                ATM.append(CO2)

        elif 22.0 > AT:
            print("Apartment temperature is too low")
            High = "False"
            ATA.append(High)
            if 21.5 > AT:
                print("Heating is on")
                CO = "True"
                ATM.append(CO)
                CO2 = "False"
                ATC.append(CO2)

ATH.sort()
LT = ATH[0]
LTStr = str(LT)
ATH.sort(reverse=True)
HT = ATH[0]
HTStr = str(HT)
TD = HT - LT
TDStr = str(TD)
print("")
print("Lowest Temperature of apartment: " + LTStr)
print("Highest Temperature of apartment: " + HTStr)
print("Difference in Temperature of apartment: " + TDStr)

for i in range(R):
    if ATA[i] == "True":
        Checker1 = ATA.count("True")
        C1str = str(Checker1)
        Problem = "The Temperature went too high " + C1str + " times"
        P.append(Problem)
    elif ATA[i] == "False":
        Checker1 = ATA.count("False")
        C1str = str(Checker1)
        Problem = "The Temperature went too low " + C1str + " times"
        P.append(Problem)
    if ATC[i] == "True":
        Checker1 = ATC.count("True")
        C1str = str(Checker1)
        Problem = "The Cooling was ON " + C1str + " times"
        P.append(Problem)
    if ATM[i] == "True":
        Checker1 = ATM.count("True")
        C1str = str(Checker1)
        Problem = "The Heating was ON " + C1str + " times"
        P.append(Problem)

if len(P) > 0:
    S = list(set(P))
    for i in S:
        print("")
        print(i)
else:
    print("No problems have occurred")
