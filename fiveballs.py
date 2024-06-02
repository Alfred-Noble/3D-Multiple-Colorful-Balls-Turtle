import turtle as t
import random

timmy = t.Turtle()
tammy = t.Turtle()
alfred = t.Turtle()
tommy = t.Turtle()
tummy = t.Turtle()


t.colormode(255)
timmy.speed("fastest")
tammy.speed("fastest")
tommy.speed("fastest")
tummy.speed("fastest")
alfred.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_need = (r, g, b)
    return random_color_need


def circle_tammy(size_gap):
    tammy.penup()
    tammy.forward(300)
    tammy.left(90)
    tammy.forward(100)
    tammy.pendown()
    for _ in range(int(360 / size_gap)):
        tammy.color(random_color())
        tammy.circle(50)
        tammy.setheading(tammy.heading() + size_gap)


def circle_tommy(size_gap):
    tommy.penup()
    tommy.left(180)
    tommy.forward(300)
    tommy.right(90)
    tommy.forward(100)
    tommy.pendown()
    for _ in range(int(360 / size_gap)):
        tommy.color(random_color())
        tommy.circle(50)
        tommy.setheading(tommy.heading() + size_gap)


def circle_tummy(size_gap):
    tummy.penup()
    tummy.forward(300)
    tummy.right(90)
    tummy.forward(120)
    tummy.pendown()
    for _ in range(int(360 / size_gap)):
        tummy.color(random_color())
        tummy.circle(50)
        tummy.setheading(tummy.heading() + size_gap)


def circle_alfred(size_gap):
    alfred.penup()
    alfred.left(180)
    alfred.forward(300)
    alfred.left(90)
    alfred.forward(120)
    alfred.pendown()
    for _ in range(int(360 / size_gap)):
        alfred.color(random_color())
        alfred.circle(50)
        alfred.setheading(alfred.heading() + size_gap)

def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        timmy.color(random_color())
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size_gap)



draw_spirograph(2)
circle_tammy(2)
circle_tommy(2)
circle_tummy(2)
circle_alfred(2)
screen = t.Screen()
screen.exitonclick()
