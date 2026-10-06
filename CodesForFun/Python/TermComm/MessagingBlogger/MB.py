import os
import sys
import hmac
import hashlib
import getpass
from pymongo import MongoClient

# Data Types and Declarations

ID = []
UserName = []
PassCode = []
UType = []

PostID = []
AuthorID = []
PostTitle = []
PostContent = []

User = ["U", "USER"]
Admin = ["A", "ADMIN"]

Off = False

# The database connection string is read from the environment so that
# no username or password is ever stored in the code.
MONGODB_URI = os.environ.get("MONGODB_URI")
if not MONGODB_URI:
    sys.exit("Set the MONGODB_URI environment variable to your MongoDB connection string first.")

# Connects to the database
MyClient = MongoClient(MONGODB_URI)

Users = MyClient["Blogging"]
LoginID = Users["LoginID"]
Posts = Users["Posts"]
ActivePosts = Users["Active Posts"]


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


def load_users():
    # Start from empty lists every time so nothing is duplicated
    ID.clear()
    UserName.clear()
    PassCode.clear()
    UType.clear()
    for x in LoginID.find():
        ID.append(x["_id"])
        UserName.append(x["UserName"])
        PassCode.append(x["PassWord"])
        UType.append(x["Type"])


def load_posts():
    PostID.clear()
    AuthorID.clear()
    PostTitle.clear()
    PostContent.clear()
    for y in Posts.find():
        PostID.append(y["_id"])
        AuthorID.append(y["AuthorID"])
        PostTitle.append(y["Title"])
        PostContent.append(y["Content"])


def next_id(prefix, collections):
    # One more than the highest number in use, so an ID is never reused
    # after a deletion (counting documents would produce a duplicate)
    highest = -1
    for collection in collections:
        for doc in collection.find({"_id": {"$regex": "^" + prefix}}):
            number = str(doc["_id"])[len(prefix):]
            if number.isdigit():
                highest = max(highest, int(number))
    return prefix + str(highest + 1).zfill(4)


def show_posts():
    print("Available Posts:")
    for i in range(len(PostID)):
        print(PostID[i] + ": " + PostTitle[i])


def read_post(Read2):
    Find = PostID.index(Read2)
    print(PostTitle[Find])
    print(PostContent[Find])


def back_or_logout():
    # Returns True if the user wants to log out
    while True:
        try:
            B = int(input("Press 1 to go back to the home page or 9 to LogOut: "))
            if B == 1:
                return False
            elif B == 9:
                return True
            else:
                print("Enter the number 1 or 9 ONLY")
        except ValueError:
            print("Enter Valid Value")


while not Off:
    load_users()
    load_posts()

    print("Welcome to the BLOGGER")
    try:
        Choice = int(input("Do you have a login ID? (1 - Yes | 0 - No | 9 - Off): "))
    except ValueError:
        print("Enter Valid Value")
        continue

    if Choice == 1:
        print("LOGIN")
        Validation = False
        GoBack = False
        while not Validation:
            UID = str(input("UserName (leave blank to go back): "))
            if UID == "":
                GoBack = True
                break
            PW = getpass.getpass(prompt='Password: ', stream=None)
            if UID in UserName and check_password(PW, PassCode[UserName.index(UID)]):
                LocBuf = UserName.index(UID)
                print("Welcome Back to BLOGGER: " + UID)
                if UType[LocBuf] == "A":
                    print("You are AN ADMIN")
                    AA = True
                    AU = False
                else:
                    print("You are A USER")
                    AA = False
                    AU = True
                UserID = ID[LocBuf]
                print("Your ID is: " + str(UserID))
                Validation = True
            else:
                print("You have entered the wrong username/password")
        if GoBack:
            continue

        LogOut = False
        while not LogOut:
            load_posts()
            if AU:
                if (len(PostID) == 0):
                    print("No Posts Available! Please Come Back Later")
                    LogOut = True
                else:
                    show_posts()
                    R2 = str(input("Enter the Post ID to read posts (To Logout, Press 9): "))
                    Read2 = R2.upper()
                    if Read2 == "9":
                        LogOut = True
                    elif Read2 in PostID:
                        read_post(Read2)
                        LogOut = back_or_logout()
                    else:
                        print("Enter Valid PostID")
            if AA:
                print("What do you want to do?")
                print("1: Create A Post")
                print("2: Delete A Post")
                print("3: Read Another Ones' Post")
                print("9: Logout")
                try:
                    Choice2 = int(input("Enter Choice: "))
                except ValueError:
                    print("Enter Valid Value")
                    continue
                if Choice2 == 1:
                    print("You have chosen: Create A Post.")
                    Title = str(input("Enter the Title of the Post: "))
                    PostTitle1 = Title.upper()
                    Content = str(input("Enter the Content of the Post: "))
                    PostContent1 = Content.lower()
                    AuID = UserID
                    PID = next_id("P", [Posts, ActivePosts])
                    Post = {"_id": PID, "AuthorID": AuID, "Title": PostTitle1, "Content": PostContent1}
                    Insert = Posts.insert_one(Post)
                    Insert2 = ActivePosts.insert_one(Post)
                    print("Post has been Created Successfully. Its ID is " + PID)
                elif Choice2 == 2:
                    if (len(PostID) == 0):
                        print("No Posts Available! Please Come Back Later")
                    else:
                        print("You have chosen: Delete A Post.")
                        show_posts()
                        ValidD = False
                        while not ValidD:
                            DID = str(input("Enter the PostID of the Post you want to delete (Press 1 to go back to home screen or Press 9 to logout): "))
                            DelID = DID.upper()
                            if DelID == "1":
                                ValidD = True
                            elif DelID == "9":
                                ValidD = True
                                LogOut = True
                            elif DelID in PostID:
                                Del = {"_id": DelID}
                                Posts.delete_one(Del)
                                ActivePosts.delete_one(Del)
                                print("Post has been Deleted Successfully.")
                                ValidD = True
                            else:
                                print("Enter the right postID")
                elif Choice2 == 3:
                    if (len(PostID) == 0):
                        print("No Posts Available! Please Come Back Later")
                    else:
                        print("You have chosen: Read Another Ones' Post.")
                        show_posts()
                        ValidRead3 = False
                        while not ValidRead3:
                            R2 = str(input("Enter the Post ID to read posts: "))
                            Read2 = R2.upper()
                            if Read2 in PostID:
                                ValidRead3 = True
                            else:
                                print("Enter Valid PostID")
                        read_post(Read2)
                        LogOut = back_or_logout()
                elif Choice2 == 9:
                    print("You have chosen: Logout")
                    print("Good Bye")
                    LogOut = True
                else:
                    print("Enter Valid Choice")
    elif Choice == 0:
        print("Create A New Account Now by filling in these details")
        Confirm1 = False
        while not Confirm1:
            Name = str(input("Name: "))
            if Name == "":
                print("Name cannot be empty")
            elif Name in UserName:
                print("UserName already Exists")
            else:
                Confirm1 = True

        Confirm2 = False
        while not Confirm2:
            Password = getpass.getpass(prompt='Password: ', stream=None)
            if len(Password) >= 8:
                Confirm2 = True
            else:
                print("Password Not Strong (use at least 8 characters)")

        Confirm3 = False
        while not Confirm3:
            Confirmation = getpass.getpass(prompt='Password Again: ', stream=None)
            if Confirmation == Password:
                Confirm3 = True
            else:
                print("Passwords don't match")
        Confirm4 = False
        while not Confirm4:
            UAC = str(input("User or Admin: "))
            UA = UAC.upper()
            if UA in User or UA in Admin:
                Confirm4 = True
            else:
                print("Enter Valid Choice")
        if UA in User:
            UOA = "U"
        else:
            UOA = "A"
        CID = next_id(UOA, [LoginID])
        Credentials = {"_id": CID, "UserName": Name, "PassWord": hash_password(Password), "Type": UOA}
        Insert = LoginID.insert_one(Credentials)
        print("Profile successfully created. Click 1 and login to BLOGGER to start blogging.")
    elif Choice == 9:
        print("Alright Good Bye!")
        Off = True
    else:
        print("Enter Valid Choice")
