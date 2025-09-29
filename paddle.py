# paddle.py
from turtle import Turtle

# Constants for paddle behavior
MOVE_DISTANCE = 20
PADDLE_TOP_LIMIT = 250
PADDLE_BOTTOM_LIMIT = -250

class Paddle(Turtle):
    """A class to represent a player's paddle."""

    def __init__(self, position):
        """
        Initializes the paddle with a specific shape, color, and position.
        :param position: A tuple (x, y) for the initial paddle location.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        # Default square is 20x20. This stretches it to be 100px tall and 20px wide.
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves the paddle up, but not past the top of the screen."""
        if self.ycor() < PADDLE_TOP_LIMIT:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down, but not past the bottom of the screen."""
        if self.ycor() > PADDLE_BOTTOM_LIMIT:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)