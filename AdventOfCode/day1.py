import re

f = open("/Users/ajvj56/MyCSJournalAJVJ/VolumeC_AdventOfCode/info.txt", "r")
Total = 0

dictionary = {
    "83": "eighth",
    "821": "eightwone",
    "218": "twoneight",
    "182": "oneightwo",
    "82": "eighttwo",
    "21": "twone",
    "18": "oneight",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

for line in f:
    for key in dictionary.keys():
        line = line.replace(dictionary[key], key)
    Nums = re.findall(r'\d+', line)
    if len(Nums) == 1:
        A = Nums[0]
        Num = A[0] + A[-1]
    else:
        B = Nums[0]
        C = Nums[-1]
        if len(B) != 1:
            B = B[0]
        if len(C) != 1:
            C = C[-1]
        Num = B + C
    print(line + " : " + Num)
    Total = Total + int(Num)

print(Total)