import turtle
from turtle import *
shape("arrow")
turtle.delay(0)
colormode(255)

for i in range(21):
    for j in range(70):
        color(255,255-j*3,255-j*3)
        forward(2)
        right(1)
    right(30)
    forward(25)
    right(162)
    for k in range(77):
        color(255,k*3,k*3)
        forward(2)
        left(1)
    # 5+(360/個数-1)
    left(168)

done()