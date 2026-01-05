import turtle
import time

t = turtle.Turtle()

for i in range(12): # Dibuat lebih kotak agar terlihat bedanya dan pergerakannya
    t.forward(30) 
    t.left(30)
    time.sleep(0.6)

turtle.done()