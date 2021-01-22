import turtle as t

def KOL(y, z, w, v, u, a):
    for x in range(y):
        t.pensize(5)
        t.pendown()
        t.forward(z)
        t.circle(w, a)
        t.penup()
        t.left(v)
        t.forward(u)
        t.pensize(1)
        t.dot()
        t.forward(u)
        t.left(v)
        t.circle(w, 180)

def KOL2(a):
    for x in range(4):
        t.pensize(5)
        t.circle(a,270)
        t.right(180)
    
t.ht()
t.bgcolor("black")
t.color("white")
KOL(4, 50, -10, -90, 10, 270)
KOL(2, 50, 15, 90, 15, 180)
t.forward(10)
t.right(90)
t.forward(10)
t.right(180)
KOL(2, 50, -15, -90, 15, 180)
t.right(180)
t.circle(15, 90)
t.right(90)
t.pendown()
KOL2(40)
t.penup()
t.right(270)
t.circle(15, 90)
t.right(180)
t.circle(10, 135)
t.left(90)
t.right(180)
t.pendown()
KOL2(45)


    
