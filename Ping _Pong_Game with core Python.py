import turtle as bot

# Set up the screen
wn = bot.Screen()
wn.title("Ping Pong Game with Mouse Control")
wn.bgcolor("black")
wn.setup(width=1000, height=800)
wn.tracer(0)  # Turns off the screen updates for manual control

# Paddle A
paddle_a = bot.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = bot.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = bot.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Function to move paddle A to the mouse position
def move_paddle_a(x, y):
    if -250 < y < 250:
        paddle_a.sety(y)

# Function to move paddle B to the mouse position
def move_paddle_b(x, y):
    if -250 < y < 250:
        paddle_b.sety(y)

# Mouse bindings
wn.listen()
wn.onscreenclick(move_paddle_a, 1)  # Left mouse button
wn.onscreenclick(move_paddle_b, 3)  # Right mouse button

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collision
    if (ball.dx > 0 and ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0 and ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
