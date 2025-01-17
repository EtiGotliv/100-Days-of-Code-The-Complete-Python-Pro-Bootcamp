import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")

def draw_spirograph(size_of_age):
    for _ in range(int(360 / size_of_age)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_age)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

#for _ in range(200):
#    tim.color(random_color())
#   tim.forward(30)
#    tim.setheading(random.choice(directions))