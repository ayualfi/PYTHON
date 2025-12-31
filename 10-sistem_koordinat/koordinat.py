import turtle


screen = turtle.Screen()
screen.title('Sistem Koordinat')

pen=turtle.Turtle()
pen.goto(100, 0)
pen.goto(0, 100)
pen.goto(-100, 0)
pen.goto(0,0)

screen.mainloop()