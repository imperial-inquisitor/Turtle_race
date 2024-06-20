from random import *
from turtle import *

def startRace(turtle,color,shape,x,y):
    turtle.color(color)
    turtle.shape(shape)
    turtle.penup()
    turtle.goto(x,y)

def geting_speed():
    return randint(1,25)

t1 = Turtle()
t2 = Turtle()
x_t1 = -300
x_t2 = -300
startRace(t1, "red", "turtle", -300,0)
startRace(t2, "blue", "turtle", -300,-50)
while x_t1 < 400 and x_t2 < 400:
    sp = geting_speed()
    t1.forward(sp)
    x_t1 += sp

    sp = geting_speed()
    t2.forward(sp)
    x_t2 += sp
if x_t1 > x_t2:
    print("Выиграла красная черепаха")
elif x_t2 > x_t1:
    print("Выиграла синяя черепаха")



exitonclick()