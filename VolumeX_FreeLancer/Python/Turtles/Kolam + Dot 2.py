import turtle as t

t.bgcolor("black")
t.color("white")

t.ht()
for y in range(2):
    if y == 0:
        t.penup()
    if y == 1:
        t.pendown()

    for x in range(2):
        t.dot()
        t.forward(50)
        t.left(45)
        t.dot()
        t.forward(70)
        t.left(-45)
        t.dot()
        t.forward(50)
        t.left(45)
        t.dot()
        t.forward(70)
        t.left(90)
        t.dot()
        t.forward(70)
        t.left(-90)
        t.dot()
        t.forward(70)
        t.left(90)
        t.dot()
        t.forward(70)
        t.left(45)
        t.dot()
        t.forward(50)
        t.left(-45)
        t.dot()
        t.forward(70)
        t.left(45)
        t.dot()

    t.penup()
    t.forward(50)
    t.left(45)
    t.forward(70)
    t.left(-45)
    t.left(180)
    t.forward(75)
    if y == 0:
        t.penup()
    if y == 1:
        t.pendown()
    t.left(225)

    for x in range(2):
        t.forward(70)
        t.left(-45)
        t.dot()
        t.forward(50)
        t.left(135)
        t.dot()
        t.forward(70)
        t.left(-90)
        t.dot()
        t.forward(70)
        t.left(135)
        t.dot()
        t.forward(50)
        t.left(-45)
        t.dot()
        t.forward(70)
        t.left(90)
        t.dot()
    if y == 0:
        t.left(45)
        t.forward(100)
        t.dot()
        t.left(-90)
        t.setx(0)
        t.sety(0)
    else:
        break



