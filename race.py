from random import *
from turtle import *

def startRace(turtle,color,shape,x,y):
    turtle.color(color)
    turtle.shape(shape)
    turtle.penup()
    turtle.goto(x,y)

def geting_speed():
    return randint(1,25)

def win_turtle(color = "черная", is_drow = False):
    t0.penup()
    t0.goto(-50,0)
    t0.pendown()
    if is_drow:
        t0.write("Выиграла дружба", font = ("SegoeUI",15, "normal"))
    else:
        t0.write("Выиграла " + color+  " черепаха", font = ("SegoeUI",15, "normal"))

t0 = Turtle()
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t0.hideturtle()
x_t1 = -300
x_t2 = -300
x_t3 = -300
startRace(t1, "red", "turtle", -300,0)
startRace(t2, "green", "turtle", -300,-50)
startRace(t3, "brown", "turtle", -300,-100)
while x_t1 < 400 and x_t2 < 400 and x_t3 <400:
    sp = geting_speed()
    t1.forward(sp)
    x_t1 += sp

    sp = geting_speed()
    t2.forward(sp)
    x_t2 += sp
    sp = geting_speed()
    t3.forward(sp)
    x_t3 += sp
if x_t1 > x_t2 and x_t1 > x_t3:
    win_turtle("красная")
elif x_t2 > x_t1 and x_t2 > x_t3:
    win_turtle("зеленая")
elif x_t3 > x_t1 and x_t3 > x_t2:
    win_turtle("коричневая")
else:
    win_turtle(is_drow = True)


exitonclick()