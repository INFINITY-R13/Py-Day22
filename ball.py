# ball.py
from turtle import Turtle

class Ball(Turtle):
    """A class to represent the ball."""

    def __init__(self):
        """Initializes the ball's appearance and movement attributes."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # x_move and y_move determine how many pixels the ball moves each frame.
        self.x_move = 10
        self.y_move = 10
        # move_speed controls the animation speed. Corresponds to time.sleep() in the main loop.
        self.move_speed = 0.1

    def move(self):
        """Moves the ball by updating its x and y coordinates."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverses the ball's vertical direction (for wall collisions)."""
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the ball's horizontal direction (for paddle collisions).
        Also increases the ball's speed each time it hits a paddle.
        """
        self.x_move *= -1
        # Decrease the sleep time by 10%, making the game loop faster.
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Resets the ball to the center of the screen after a player scores.
        Also resets the speed and serves the ball to the opposite player.
        """
        self.goto(0, 0)
        self.move_speed = 0.1  # Reset the speed to the initial value.
        self.bounce_x()        # Reverse direction to serve to the other player.