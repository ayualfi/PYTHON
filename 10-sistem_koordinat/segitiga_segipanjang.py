import turtle

jendela = turtle.Screen()
jendela.title('Segitiga dan Persegi panjang')

# turtle pertama
t1 = turtle.Turtle()
t1.goto(200, 0)
t1.goto(0, 200)
t1.goto(-200, 0)
t1.goto(0,0)

#turtle kedua
t2 = turtle.Turtle()

t2.penup()
t2.goto(0, -150)
t2.pendown()

t2.forward(200)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(400)
t2.left(90)
t2.forward(100)
t2.goto(0,-150)

turtle.done()