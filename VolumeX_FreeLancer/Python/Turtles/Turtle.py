import turtle as t

t.penup()
t.ht()
T = int(input("Enter Length of Triangle: "))
z = int((T+1)/2)
for dot in range(z):
    if T>9:
        t.goto(-25*dot, 0)
    elif T>49:
        t.goto(-1*dot, 0)
    else:
        t.goto(-50*dot, 0)
    for x in range(3):
        t.left(120)
        for y in range(T-(2*dot)):
            t.dot()
            if T>9:
                t.forward(10)
            elif T>50:
                t.forward(1)
            else:
                t.forward(50)
