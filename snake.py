
import turtle
import random
import time

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("#E6F3FF")
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#228B22")
head.shapesize(1.1, 1.1)
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#FF4500")
food.shapesize(1.1, 1.1)
food.penup()
food.goto(0, 100)

segments = []
score = 0
delay = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#2F4F4F")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 18, "bold"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

border = turtle.Turtle()
border.speed(0)
border.color("#87CEEB")
border.penup()
border.goto(-290, -290)
border.pendown()
border.pensize(4)
for _ in range(4):
    border.forward(580)
    border.left(90)
border.hideturtle()

while True:
    window.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Arial", 18, "bold"))

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#32CD32")
        new_segment.shapesize(1.1, 1.1)
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Arial", 18, "bold"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Arial", 18, "bold"))

    time.sleep(delay)

window.mainloop()
