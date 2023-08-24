import turtle
import random
r=turtle.Screen()
aryan=turtle.Turtle()
r.colormode(225)
aryan.speed(0)
aryan.width(2)
r.bgcolor("blue")
aryan.pencolor("orange")
def shape(angle,side,limit):
    reverseDirection=200
    aryan.forward(side)
    if side%(reverseDirection*2)==0:
        angle=angle+2
    elif side%reverseDirection==0:
        angle=angle-2
        print('side')
    aryan.right(angle)
    side=side+2
    if side<limit:
        shape(angle,side,limit)
angle=165
side=-5
limit=1000
shape(angle,side,limit)
turtle.done()