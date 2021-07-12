from turtle import *
color('green')
bgcolor('black')
speed(10)
wn = Screen()
wn.title("COVID-19")
hideturtle()
b = 0 
while b < 200:
	right(b)
	forward (b * 3)
	b = b + 1