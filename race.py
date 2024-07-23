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
    t0.goto(-80,100)
    t0.pendown()
    if is_drow:
        t0.write("Выиграла дружба", font = ("SegoeUI",15, "normal"))
    else:
        t0.write("Выиграла " + color+  " черепаха", font = ("SegoeUI",15, "normal"))

def road():
    t0.speed(0)
    t0.color("grey")
    t0.pensize(20)
    t0.penup()
    t0.goto(-340,55)
    t0.pendown()
    for i in range(2):
        t0.forward(840)
        t0.right(90)
        t0.forward(230)
        t0.right(90)
    t0.pensize(2)
    t0.right(90)
    x = -280
    for i in range(78):
        t0.penup()
        t0.goto(x,55)
        t0.pendown()
        x+=10
        t0.forward(230)

def question_turtle(option):
    t0.penup()
    t0.goto(-80, 80)
    t0.pendown()
    if question == option:
        t0.write("Угадал", font= ("SegoeUI",15, "normal"))
    else:
        t0.write("Лох", font= ("SegoeUI",15, "normal"))

t0 = Turtle()
road()
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
question = input("Назови цвет черепашки, которая выиграет ").lower()
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
    t0.color("red")
    win_turtle("красная")
    question_turtle("красная")
elif x_t2 > x_t1 and x_t2 > x_t3:
    t0.color("green")
    win_turtle("зеленая")
    question_turtle("зеленая")
elif x_t3 > x_t1 and x_t3 > x_t2:
    t0.color("brown")
    win_turtle("коричневая")
    question_turtle("коричневая")
else:
    win_turtle(is_drow = True)
    t0.color("black")
    question_turtle("ничья")


exitonclick()