#File Management
print("Opening blocklist.txt\n")
try:
    bl = open("UniDays/Volume2_IE0005/Volume1_Week1/Exercise0/blocklist.txt", "r+")
except FileNotFoundError:
    print("File does not exist! Creating blocklist.txt")
    bl = open("UniDays/Volume2_IE0005/Volume1_Week1/Exercise0/blocklist.txt", "x+")

print("Opening visitors.txt\n")
try:
    v = open("UniDays/Volume2_IE0005/Volume1_Week1/Exercise0/visitors.txt", "r+")
except FileNotFoundError:
    print("File does not exist! Creating visitors.txt")
    v = open("UniDays/Volume2_IE0005/Volume1_Week1/Exercise0/visitors.txt", "x+")


blocklists = bl.read().splitlines()
visitors = v.read().splitlines()

Violation = "alice@wonderland.co.uk"

print("A user {} has offended the site rules!".format(Violation))

bl.write("\n" + Violation)
blocklists.append(Violation)

bl.close()
v.close()

#Main Code

print("\nBLOCKED LIST\n")
for x in blocklists:
    print(x)

print("\nVISITORS\n")
print(str(len(visitors)) + " have visited the website!")
for x in visitors:
    if x in blocklists:
        print(x + " is a blocked ID and has not been allowed access!")
