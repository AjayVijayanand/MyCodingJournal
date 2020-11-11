Accepted = 0
Rejected = 0
TotalPrice = 0
Correct0 = False
while not Correct0:
    try:
        ParcelCount = int(input("Enter Number of Parcels: "))
        if ParcelCount > 0:
            Correct0 = True
        else:
            print("Enter Valid Value")
    except ValueError:
        print("Enter Valid Value")

for i in range(ParcelCount):
    print("Enter dimensions and weight for parcel " + str(i+1))
    Correct1 = False
    while not Correct1:
        try:
            ParcelHeight = float(input("Enter Height of Parcel: "))
            if ParcelHeight > 0:
                Correct1 = True
            else:
                print("Enter Valid Value")
        except ValueError:
            print("Enter Valid Value")

    Correct2 = False
    while not Correct2:
        try:
            ParcelWidth = float(input("Enter Width of Parcel: "))
            if ParcelWidth > 0:
                Correct2 = True
            else:
                print("Enter Valid Value")
        except ValueError:
            print("Enter Valid Value")

    Correct3 = False
    while not Correct3:
        try:
            ParcelLength = float(input("Enter Length of Parcel: "))
            if ParcelLength > 0:
                Correct3 = True
            else:
                print("Enter Valid Value")
        except ValueError:
            print("Enter Valid Value")

    Correct4 = False
    while not Correct4:
        try:
            ParcelWeight = float(input("Enter Weight of Parcel: "))
            if ParcelLength > 0:
                Correct4 = True
            else:
                print("Enter Valid Value")
        except ValueError:
            print("Enter Valid Value")
    ParcelDimension = ParcelLength + ParcelHeight + ParcelWidth
    if (ParcelHeight < 80 and ParcelWidth < 80 and ParcelLength < 80) and (1 <= ParcelWeight <= 10 ) and ParcelDimension < 200:
        print("Parcel Accepted")
        Accepted = Accepted + 1
        if 1 <= ParcelWeight <= 5:
            ParcelCost = 10
        else:
            ParcelWeightExceed = 10 - ParcelWeight
            Multiplier = ParcelWeightExceed/0.1
            ParcelCost = 10 + (Multiplier * 0.10)
        print("Price of Parcel: $" + str(ParcelCost))
        TotalPrice = TotalPrice + ParcelCost
    else:
        print("Parcel has been rejected")
        rejected = Rejected + 1
        if ParcelHeight >= 80:
            print("Parcel's Height is more than 80cm")
        if ParcelLength >= 80:
            print("Parcel's Length is more than 80cm")
        if ParcelWidth >= 80:
            print("Parcel's Width is more than 80cm")
        if 1 > ParcelWeight:
            print("Weight is less than 1kg")
        if 10 < ParcelWeight:
            print("Weight is more than 10kg")
        if ParcelDimension >= 200:
            print("Total Dimension is more than 200cm")

print("Parcels Accepted: " + str(Accepted))
print("Parcels Rejected: " + str(Rejected))
print("Total Cost: " + str(TotalPrice))










