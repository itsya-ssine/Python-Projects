import turtle
import time
import random

delay = 0.08
fps = 20

score = 0
high_score = 0

try:
    with open("score.txt", 'r') as file:
        high_score = int(file.readline())
except:
    pass

app = turtle.Screen()
app.title("Snake Game")
app.bgcolor("green")
app.setup(600, 600)
app.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.goto(0, 260)
pen.clear()
pen.write(f"Score: 0  High Score: {high_score}",
          align="center",
          font=("Courier", 16, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+fps)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-fps)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+fps)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-fps)

def restart():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for seg in segments:
        seg.goto(1000, 1000)

    segments.clear()

    with open("score.txt", 'w') as file:
        file.write(f"{high_score}")

    score = 0
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center",
                  font=("Courier", 16, "normal"))

app.listen()
app.onkeypress(go_up, "z")
app.onkeypress(go_down, "s")
app.onkeypress(go_right, "d")
app.onkeypress(go_left, "q")

while True:
    app.update()

    if head.xcor() >  290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        restart()

    for seg in segments:
        if head.distance(seg) < 20:
            restart()

    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 13) * 20
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center",
                  font=("Courier", 16, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(delay)
