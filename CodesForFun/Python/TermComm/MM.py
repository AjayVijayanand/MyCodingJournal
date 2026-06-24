import platform
from pymongo import MongoClient
import datetime
import subprocess as sp

MyClient = MongoClient("mongodb+srv://USER:PASSWORD@cluster0.x2hph.mongodb.net/?retryWrites=true&w=majority")
Users = MyClient["Messaging"]
LoginID = Users["People"]
Posts = Users["Messages"]
Off = False
TIME = datetime.datetime.now()
Username = []
Password = []
Sender = []
Messages = []
Time_Of_Message = []
while not Off:
    Users = MyClient["Messaging"]
    LoginID = Users["People"]
    Posts = Users["Messages"]
    for x in LoginID.find():
        Username.append(x["USERNAME"])
        Password.append(x["PASSWORD"])
    for y in Posts.find():
        Sender.append(y["Sender"])
        Messages.append(y["Messages"])
        Time_Of_Message.append(y["Time_Of_Message"])
    print("Welcome to Public Messaging")
    Choice = str(input("Do you have a Username? (1 - Yes|0 - No|~ - Exit): "))
    if Choice == "1":
        Validation1 = False
        while not Validation1:
            try:
                User = str(input("Enter your Username: "))
                Pass = str(input("Enter your Password: "))
                if User in Username and Pass == Password[Username.index(User)]:
                    Validation1 = True
                else:
                    print("Username or Password is wrong!")
            except ValueError:
                print("Enter Valid Value")
        W = "Welcome " + User
        V = User + " Has Left the Chat"
        MsgerData1 = {"Sender": User, "Messages": W, "Time_Of_Message": TIME.strftime("%X")}
        Posts.insert_one(MsgerData1)
        Exit = False
        while not Exit:
            Refresh = False
            while not Refresh:
                Sender = []
                Messages = []
                Time_Of_Message = []
                for y in Posts.find():
                    Sender.append(y["Sender"])
                    Messages.append(y["Messages"])
                    Time_Of_Message.append(y["Time_Of_Message"])
                if platform.system().lower()=="windows":
                    cmd='cls'
                else:
                    cmd='clear'
                sp.call(cmd, shell=True)
                TIME = datetime.datetime.now()
                for z in range(len(Messages)):
                    if Messages[z] == ("Welcome" + Sender[z]):
                        print(Messages[z])
                    elif Messages[z] == (Sender[z] + " Has Left the Chat"):
                        print(Messages[z])
                    else:
                        print(Sender[z] + " (Sent on " + Time_Of_Message[z] + "): " + Messages[z])
                Msg = str(input("Type in a message(Enter ~ to exit. Press Enter to refresh. Last Refresh was at " + TIME.strftime("%X") + "): "))
                if Msg != "~" and Msg != "":
                    MsgerData2 = {"Sender": User, "Messages": Msg, "Time_Of_Message": TIME.strftime("%X")}
                    Posts.insert_one(MsgerData2)
                    Refresh = True
                elif Msg == "~":
                    print(V)
                    MsgerData3 = {"Sender": User, "Messages": V, "Time_Of_Message": TIME.strftime("%X")}
                    Refresh = True
                    Exit = True
                elif Msg == "":
                    print("")
                    Refresh = True
    elif Choice == "0":
        NewUser = str(input("Enter a UserName: "))
        NewPassword = str(input("Enter Password: "))
        NewData = {"USERNAME": NewUser, "PASSWORD": NewPassword}
        LoginID.insert_one(NewData)
    elif Choice == "~":
        print("BYE BYE")
        Off = True
