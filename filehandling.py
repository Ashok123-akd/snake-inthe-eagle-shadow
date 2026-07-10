'''
-------------------------file handling day -10 --------------------------------------------------------------
file = open("student.txt")
print(file.read()) - reads everything at once
print(file.readline()) - one line at a time
print(file.readlines())- a last of lines 

usingwrite()****************************

file = open("notes.txt","w")
file.write("HELLO KAT")
file.write("\nPython is a snake!")
file.close()

closing files*****************************

file = open("notes.txt","r")
print(file.read())
file.close

best case********************************

with open("notes.txt,"r")as file:
    print((file.read))
#file is closed automatically here

graphics*****************************
import turtle
a =0
b=0
turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("green")
turtle.penup()
turtle.goto(0,200)
turtle.pendown()

while True:
    turtle.forward(a)
    turtle.right(b)
    a=a+3
    b=b+1
    if b==210:
     break
turtle.exitonclick()


'''

# star graphics 

from turtle import *
from colorsys import *

speed(0)
bgcolor("black")
tracer(2)
pensize(1)

for i in range(350):
    color(hsv_to_rgb(i/150,1,1))
    up()
    forward(i*0.8)
    right(59)
    down()
    size = 5 + i * 0.1
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()
done()
