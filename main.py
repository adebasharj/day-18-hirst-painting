from turtle import Screen
import random
import turtle as turtle_module

turtle_module.colormode(255)
jack = turtle_module.Turtle()
jack.speed('fastest')
jack.penup()
jack.hideturtle()

color_list = [(5, 12, 35), (40, 21, 16), (130, 89, 54), (202, 137, 119), (235, 211, 82), (188, 137, 161), (216, 83, 67),
           (80, 6, 20), (33, 139, 65), (147, 86, 105), (193, 77, 101), (29, 87, 29), (220, 176, 210), (74, 107, 141),
           (152, 136, 65), (20, 207, 180), (12, 72, 28), (132, 158, 180), (7, 62, 139), (114, 188, 158), (86, 133, 173),
           (125, 8, 28), (18, 204, 220), (242, 204, 6), (236, 172, 164), (133, 223, 208)]

jack.setheading(255)
jack.forward(300)
jack.setheading(0)
dot_number = 101

for dot_count in range(1, dot_number):
    jack.dot(20, random.choice(color_list))
    jack.forward(50)

    if dot_count % 10 == 0:
        jack.setheading(90)
        jack.forward(50)
        jack.setheading(180)
        jack.forward(500)
        jack.setheading(0)

screen = Screen()
screen.exitonclick()