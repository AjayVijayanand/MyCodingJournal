import numpy
import matplotlib.pyplot as plt
from scipy import stats
import time

def myfunc(x):
  return slope * x + intercept

Bot = []
User = []

for x in range(8):
    UI = 0
    while not(1 <= UI <= 6):
        try:
            UI = int(input("Enter Num: "))
        except ValueError:
            print("Enter Valid Value!")
    User.append(UI)
    BI = numpy.random.randint(1, 7)
    Bot.append(BI)

print("Bot Values[x]: " + str(Bot[:8]))
print("User Values[y]]: " + str(User[:8]))

slope, intercept, r, p, std_err = stats.linregress(User[:8], Bot[:8])

mymodel = list(map(myfunc, User))

Sync = round(r*100, 1)
if Sync < 0:
    Sync = -Sync

print("Regression: " + str(r))
print("Slope: " + str(slope))
print("Intercept: " + str(intercept))
print("Probability: " + str(p))
print("Standard Error: " + str(std_err))
print("Bot Accuracy: " + str(Sync) + "%")

plt.scatter(User[:8], Bot[:8])
plt.plot(User, mymodel)
plt.show()

#-----------
print("Testing Time")
for x in range(2):
    UI = 0
    while not(1 <= UI <= 6):
        try:
            UI = int(input("Enter Num: "))
        except ValueError:
            print("Enter Valid Value!")
    User.append(UI)
    BI = round(myfunc(UI))
    Bot.append(BI)
    if UI == BI:
        print("They are Equal!")

print("Bot Values[x]: " + str(Bot[8:]))
print("User Values[y]: " + str(User[8:]))

plt.scatter(User[8:], Bot[8:])
plt.show()

