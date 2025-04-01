import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Caterpillar Game")
screen.setup(width=600, height=600)
screen.tracer(0)

# Caterpillar setup
segments = []
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"
segments.append(head)

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-250, 250), random.randint(-250, 250))

# Score tracking
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Movement functions
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

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

# Collision with food
def check_collision_with_food():
    global score
    if head.distance(food) < 20:
        food.goto(random.randint(-250, 250), random.randint(-250, 250))
        add_segment()
        score += 10
        update_score()

# Add a segment to the caterpillar
def add_segment():
    new_segment = turtle.Turtle()
    new_segment.shape("square")
    new_segment.color("lightgreen")
    new_segment.penup()
    segments.append(new_segment)

# Update score
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Collision with walls or self
def check_collision():
    if (
        head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290
    ):
        return True
    for segment in segments[1:]:
        if head.distance(segment) < 20:
            return True
    return False

# Update segments
def update_segments():
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

# Keyboard bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Main game loop
game_running = True
while game_running:
    screen.update()
    move()
    check_collision_with_food()
    update_segments()
    if check_collision():
        game_running = False

# Game over
game_over = turtle.Turtle()
game_over.color("red")
game_over.hideturtle()
game_over.write("GAME OVER", align="center", font=("Courier", 36, "bold"))

# Keep the window open
screen.mainloop()
