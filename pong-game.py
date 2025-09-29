# main.py
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# --- CONSTANTS --- #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_RIGHT_POS = (350, 0)
PADDLE_LEFT_POS = (-350, 0)
WALL_TOP_Y = 280
WALL_BOTTOM_Y = -280
PADDLE_COLLISION_X = 320
BALL_OUT_OF_BOUNDS_X = 380

# 1. Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)  # Turn off automatic screen updates

# 2. Create game objects (paddles, ball, scoreboard)
r_paddle = Paddle(PADDLE_RIGHT_POS)
l_paddle = Paddle(PADDLE_LEFT_POS)
ball = Ball()
scoreboard = Scoreboard()

# 3. Set up key listeners
screen.listen()
# Right paddle controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Left paddle controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# 4. Main game loop
game_is_on = True
while game_is_on:
    # The 'move_speed' is the sleep interval. A smaller number makes the game faster.
    time.sleep(ball.move_speed)
    screen.update()  # Manually update the screen
    ball.move()

    # Detect collision with top or bottom wall
    if ball.ycor() > WALL_TOP_Y or ball.ycor() < WALL_BOTTOM_Y:
        ball.bounce_y()

    # Detect collision with a paddle
    # Checks distance from the center of the ball to the center of the paddle AND
    # ensures the ball is in front of the paddle's x-coordinate.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > PADDLE_COLLISION_X) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -PADDLE_COLLISION_X):
        ball.bounce_x()

    # Detect when the right paddle misses the ball
    if ball.xcor() > BALL_OUT_OF_BOUNDS_X:
        ball.reset_position()  # Reset ball to center
        scoreboard.l_point()   # Left player gets a point

    # Detect when the left paddle misses the ball
    if ball.xcor() < -BALL_OUT_OF_BOUNDS_X:
        ball.reset_position()  # Reset ball to center
        scoreboard.r_point()   # Right player gets a point

# Exit the game when the screen is clicked
screen.exitonclick()