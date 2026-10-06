import os
import sys
import hmac
import hashlib
import getpass
import platform
import datetime
import subprocess as sp
from pymongo import MongoClient

# The database connection string is read from the environment so that
# no username or password is ever stored in the code.
MONGODB_URI = os.environ.get("MONGODB_URI")
if not MONGODB_URI:
    sys.exit("Set the MONGODB_URI environment variable to your MongoDB connection string first.")


def hash_password(password):
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200000)
    return "pbkdf2$" + salt.hex() + "$" + digest.hex()


def check_password(password, stored):
    if stored.startswith("pbkdf2$"):
        _, salt, digest = stored.split("$")
        attempt = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), 200000)
        return hmac.compare_digest(attempt.hex(), digest)
    # Accounts made before passwords were hashed
    return hmac.compare_digest(password, stored)


def clear_screen():
    if platform.system().lower() == "windows":
        cmd = 'cls'
    else:
        cmd = 'clear'
    sp.call(cmd, shell=True)


MyClient = MongoClient(MONGODB_URI)
Users = MyClient["Messaging"]
LoginID = Users["People"]
Posts = Users["Messages"]
Off = False

while not Off:
    Username = []
    Password = []
    for x in LoginID.find():
        Username.append(x["USERNAME"])
        Password.append(x["PASSWORD"])
    print("Welcome to Public Messaging")
    Choice = str(input("Do you have a Username? (1 - Yes|0 - No|~ - Exit): "))
    if Choice == "1":
        Validation1 = False
        GoBack = False
        while not Validation1:
            User = str(input("Enter your Username (leave blank to go back): "))
            if User == "":
                GoBack = True
                break
            Pass = getpass.getpass(prompt="Enter your Password: ")
            if User in Username and check_password(Pass, Password[Username.index(User)]):
                Validation1 = True
            else:
                print("Username or Password is wrong!")
        if GoBack:
            continue
        W = "Welcome " + User
        V = User + " Has Left the Chat"
        TIME = datetime.datetime.now()
        MsgerData1 = {"Sender": User, "Messages": W, "Time_Of_Message": TIME.strftime("%X")}
        Posts.insert_one(MsgerData1)
        Exit = False
        while not Exit:
            Sender = []
            Messages = []
            Time_Of_Message = []
            for y in Posts.find():
                Sender.append(y["Sender"])
                Messages.append(y["Messages"])
                Time_Of_Message.append(y["Time_Of_Message"])
            clear_screen()
            TIME = datetime.datetime.now()
            for z in range(len(Messages)):
                if Messages[z] == ("Welcome " + Sender[z]):
                    print(Messages[z])
                elif Messages[z] == (Sender[z] + " Has Left the Chat"):
                    print(Messages[z])
                else:
                    print(Sender[z] + " (Sent on " + Time_Of_Message[z] + "): " + Messages[z])
            Msg = str(input("Type in a message(Enter ~ to exit. Press Enter to refresh. Last Refresh was at " + TIME.strftime("%X") + "): "))
            if Msg == "~":
                print(V)
                MsgerData3 = {"Sender": User, "Messages": V, "Time_Of_Message": TIME.strftime("%X")}
                Posts.insert_one(MsgerData3)
                Exit = True
            elif Msg != "":
                MsgerData2 = {"Sender": User, "Messages": Msg, "Time_Of_Message": TIME.strftime("%X")}
                Posts.insert_one(MsgerData2)
    elif Choice == "0":
        NewUser = str(input("Enter a UserName: "))
        if NewUser == "":
            print("UserName cannot be empty")
        elif NewUser in Username:
            print("UserName already Exists")
        else:
            NewPassword = getpass.getpass(prompt="Enter Password: ")
            NewData = {"USERNAME": NewUser, "PASSWORD": hash_password(NewPassword)}
            LoginID.insert_one(NewData)
            print("Account created. Enter 1 to log in.")
    elif Choice == "~":
        print("BYE BYE")
        Off = True
    else:
        print("Enter Valid Choice")
