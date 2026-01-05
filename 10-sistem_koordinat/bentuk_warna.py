import turtle
import time


t2 = turtle.Turtle()
t2.color('#fc03ba', '#fc8ddf')
time.sleep(0.90)
points = [
    (0, 140),
    (-80, 160),
    (-130, 100),
    (-140, 40),
    (-110, 0),
    (-40,-60),
    (0, -90),
    (40, -60),
    (110,0),
    (140,40),
    (130,100),
    (80, 160),
    (0, 140)
]
t2.begin_fill() #agar warna nya nge fill
for x, y in points:
    t2.goto(x,y)
t2.end_fill() #agar warna nya nge fill



t1 = turtle.Turtle()
t1.penup()
t1.goto(-50, -230)
t1.pendown()
t1.color('#2d529c', "#fff700")
t1.begin_fill()
for i in range(4):
    t1.forward(100)
    t1.left(90)
t1.end_fill()

turtle.done()