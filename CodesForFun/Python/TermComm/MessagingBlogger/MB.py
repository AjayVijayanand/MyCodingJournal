from pymongo import MongoClient
import ssl
import getpass
# Data Types and Declarations

ID = []
UserName = []
PassCode = []
UType = []

PostID = []
AuthorID = []
PostTitle = []
PostContent = []
PostViews = []

User = ["U", "USER"]
Admin = ["A", "ADMIN"]

Off = False

# Connects to the database
MyClient = MongoClient(
    "mongodb+srv://AJVJ:gamer9AJAY@cluster0.x2hph.mongodb.net/?retryWrites=true&w=majority")

Users = MyClient["Blogging"]
LoginID = Users["LoginID"]
Posts = Users["Posts"]
ActivePosts = Users["Active Posts"]

while not Off:
    for x in LoginID.find():
        ID.append(x["_id"])
        UserName.append(x["UserName"])
        PassCode.append(x["PassWord"])
        UType.append(x["Type"])

    for y in Posts.find():
        PostID.append(y["_id"])
        AuthorID.append(y["AuthorID"])
        PostTitle.append(y["Title"])
        PostContent.append(y["Content"])

    print("Welcome to the BLOGGER")
    try:
        Choice = int(input("Do you have a login ID? (1 - Yes | 0 - No | 9 - Off): "))
        if Choice == 1:
            print("LOGIN")
            Validation = False
            while not Validation:
                try:
                    UID = str(input("UserName: "))
                    PW = str(input("Password: "))
                    if UID in UserName and PW in PassCode:
                        for x in UserName:
                            if x == UID:
                                FName = x
                                LocBuf = UserName.index(UID)
                                break
                        if PW == PassCode[LocBuf]:
                            print("Welcome Back to BLOGGER: " + FName)
                            if UType[LocBuf] == "U":
                                print("You are A USER")
                                AA = False
                                AU = True
                            elif UType[LocBuf] == "A":
                                print("You are AN ADMIN")
                                AA = True
                                AU = False
                            UserID = ID[LocBuf]
                            print("Your ID is: " + UserID)
                            Validation = True
                    else:
                        print("You have entered the wrong username/password")
                except ValueError:
                    print("Enter Valid Value")
            LogOut = False
            while not LogOut:
                if AU:
                    if (len(PostID) == 0):
                        print("No Posts Available! Please Come Back Later") 
                    else:
                        ValidRead2 = False
                        while not ValidRead2:
                            try:
                                R2 = str(input("Enter the Post ID to read posts (To Logout, Press 9): "))
                                Read2 = R2.upper()
                                if Read2 in PostID:
                                    ValidRead2 = True
                                if Read2 == 9:
                                    ValidRead2 = True
                                    LogOut = True
                                else:
                                    print("Enter Valid PostID")
                            except ValueError:
                                print("Enter Valid Value")

                        Find = PostID.index(Read2)
                        print(PostTitle[Find])
                        print(PostContent[Find])
                        Valid = False
                        while not Valid:
                            try:
                                B = int(input("Press 1 to go back to the home page or 9 to LogOut"))
                                if B == 1:
                                    Valid = True
                                elif B == 9:
                                    Valid = True
                                    LogOut = True
                                else:
                                    print("Enter the number 1 or 9 ONLY")
                            except ValueError:
                                print("Enter Valid Value")
                if AA:
                    print("What do you want to do?")
                    print("1: Create A Post")
                    print("2: Delete A Post")
                    print("3: Read Another Ones' Post")
                    print("9: Logout")
                    Choice2 = int(input("Enter Choice: "))
                    if Choice2 == 1:
                        print("You have chosen: Create A Post.")
                        Title = str(input("Enter the Title of the Post: "))
                        PostTitle1 = Title.upper()
                        Content = str(input("Enter the Content of the Post: "))
                        PostContent1 = Content.lower()
                        AuID = UserID
                        Query = {"_id": {"$regex": "^P"}}
                        P = str(Posts.count_documents(Query))
                        Num = str(P).zfill(4)
                        PID = "P" + Num
                        Post = {"_id": PID, "AuthorID": AuID, "Title": PostTitle1, "Content": PostContent1}
                        Insert = Posts.insert_one(Post)
                        Insert2 = ActivePosts.insert_one(Post)
                        print("Post has been Created Successfully.")
                    elif Choice2 == 2:
                        if (len(PostID) == 0):
                            print("No Posts Available! Please Come Back Later") 
                        else:
                            print("You have chosen: Delete A Post.")
                            ValidD = False
                            RetHome = False
                            while not ValidD:
                                try:
                                    DID = str(input("Enter the PostID of the Post you want to delete (Press 1 to go back to home screen or Press 9 to logout): "))
                                    for v in PostID:
                                        print(v)
                                    DelID = DID.upper()
                                    if DelID in PostID:
                                        ValidD = True
                                    elif DelID == 1:
                                        ValidD = True
                                        RetHome = True
                                    elif DelID == 9:
                                        ValidID = True
                                        RetHome = True
                                        LogOut = True
                                    else:
                                        print("Enter the right postID")
                                except ValueError:
                                    print("Enter Valid Value")
                                if not RetHome:
                                    Del = {"_id": DelID}
                                    Posts.delete_one(Del)
                                    print("Post has been Deleted Successfully.")
                    elif Choice2 == 3:
                        print("You have chosen: Read Another Ones' Post.")
                        ValidRead3 = False
                        while not ValidRead3:
                            try:
                                R2 = str(input("Enter the Post ID to read posts: "))
                                Read2 = R2.upper()
                                if Read2 in PostID:
                                    ValidRead3 = True
                                else:
                                    print("Enter Valid PostID")
                            except ValueError:
                                print("Enter Valid Value")

                        Find = PostID.index(Read2)
                        print(PostTitle[Find])
                        print(PostContent[Find])
                        Valid = False
                        while not Valid:
                            try:
                                B = int(input("Press 1 to go back to the home page or 9 to Logout"))
                                if B == 1:
                                    Valid = True
                                elif B == 9:
                                    Valid = True
                                    LogOut = True
                                else:
                                    print("Enter the number 1 or 9 ONLY")
                            except ValueError:
                                print("Enter Valid Value")
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
                try:
                    Name = str(input("Name: "))
                    if Name in UserName:
                        print("UserName already Exists")
                    else:
                        Confirm1 = True
                except ValueError:
                    print("Enter Valid Value")

            Confirm2 = False
            while not Confirm2:
                try:
                    Password = getpass.getpass(prompt='Password: ', stream=None)
                    if len(Password) >= 8:
                        Confirm2 = True
                    else:
                        print("Password Not Strong")
                except ValueError:
                    print("Enter Valid Value")

            Confirm3 = False
            while not Confirm3:
                try:
                    Confirmation = getpass.getpass(prompt='Password Again: ', stream=None)
                    if Confirmation == Password:
                        Confirm3 = True
                    else:
                        print("Passwords don't match")
                except ValueError:
                    print("Enter Valid Value")
            Confirm4 = False
            while not Confirm4:
                try:
                    UAC = str(input("User or Admin: "))
                    UA = UAC.upper()
                    if UA in User or UA in Admin:
                        Confirm4 = True
                    else:
                        print("Enter Valid Choice")
                except ValueError:
                    print("Enter Valid Value")
            if UA in User:
                UOA = "U"
                Query = {"Type": {"$regex": "^U"}}
            elif UA in Admin:
                UOA = "A"
                Query = {"Type": {"$regex": "^A"}}
            ID1 = str(LoginID.count_documents(Query))
            Info = str(ID1).zfill(4)
            CID = UOA + Info
            Credentials = {"_id": CID, "UserName": Name, "PassWord": Password, "Type": UOA}
            Insert = LoginID.insert_one(Credentials)
            print("Profile successfully created. Click 1 and login to BLOGGER to start blogging.")
        elif Choice == 9:
            print("Alright Good Bye!")
            Off = True
        else:
            print("Enter Valid Choice")
    except ValueError:
        print("Enter Valid Value")