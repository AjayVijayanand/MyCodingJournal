import turtle as t
import random


def SimpleDes(n, l):
    for y in range(n):
        t.pencolor(random.randint(0, 255), random.randint(50, 255), random.randint(0, 255))
        t.penup()
        t.goto(0, 0)
        a = ((n-2) * 360) / n
        t.right(a*n)
        t.pendown()
        t.circle(l, 90)
        if n%2 == 0:
            t.left(a)
        else:
            t.left(a + 90)

t.ht()
t.colormode(255)
t.bgcolor(0, 0, 0)
t.speed(0)
for z in range(3, 100):
    t.right(random.randint(0, 360))
    SimpleDes(z, random.randint(100, 500))