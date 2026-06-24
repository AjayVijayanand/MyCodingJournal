import turtle as t

def Recursion (side, length, n):
    t.colormode(255)
    t.ht()
    t.speed(10)
    t.bgcolor(0, 0, 0)
    t.penup()
    t.goto(-300, -300)
    t.pendown()
    angle = 180 - (((side - 2) * 180) / side)
    r = g = b = 255
    for y in range(n):
        length = length * 0.98
        r = abs(int(r - (255/n)))
        g = abs(int(g - (255/n)))
        b = abs(int(b - (255/n)))
        if y == 0 or y == 1:
            t.pencolor(255, 255, 255)
        if y % 2 == 0:
            t.pencolor(r, 255, 255)
        if y % 3 == 0:
            t.pencolor(r, g, 255)
        if y % 5 == 0:
            t.pencolor(255, g, b)
        if y % 7 == 0:
            t.pencolor(255, g, 255)
        if y % 11 == 0:
            t.pencolor(255, 255, b)
        for x in range(side + 1):
            t.forward(length)
            t.left(angle)

Recursion(10, 200, 255)