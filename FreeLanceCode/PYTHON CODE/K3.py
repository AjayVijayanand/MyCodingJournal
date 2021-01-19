import turtle
import time

y = 0.25
turtle.ht()
turtle.penup()

turtle.goto(-90, 90)
for x in range(5):
    time.sleep(y)
    turtle.dot()
    turtle.fd(45)

turtle.goto(-45, 45)
for x in range(3):
    time.sleep(y)
    turtle.dot()
    turtle.fd(45)

turtle.goto(-45, 135)
for x in range(3):
    time.sleep(y)
    turtle.dot()
    turtle.fd(45)

turtle.goto(0, 0)
time.sleep(y)
turtle.dot()

turtle.goto(0, 180)
time.sleep(y)
turtle.dot()

turtle.goto(0, 45)


turtle.pendown()
time.sleep(y)
turtle.left(45)
turtle.fd(64)
for x in range (3):
    time.sleep(y)
    turtle.left(90)
    turtle.fd(64)
turtle.left(-45)

time.sleep(y)
turtle.forward(45)
turtle.left(135)
time.sleep(y)
turtle.forward(64)
turtle.left(45)
time.sleep(y)
turtle.forward(45)
for x in range(3):
    time.sleep(y)
    turtle.left(-90)
    turtle.forward(45)
    time.sleep(y)
    turtle.left(135)
    turtle.forward(63)
    time.sleep(y)
    turtle.left(45)
    turtle.forward(45)

turtle.penup()
turtle.goto(0, 80)
turtle.pendown()
turtle.circle(10)
