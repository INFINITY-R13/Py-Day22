# scoreboard.py
from turtle import Turtle

# Constants for scoreboard appearance
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    """A class to manage and display the score."""

    def __init__(self):
        """Initializes the scoreboard's appearance and scores."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # We only want to see the text, not the turtle object.
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the old score and writes the new score on the screen."""
        self.clear()  # Clear previous score before writing the new one.
        # Position and write the left player's score
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        # Position and write the right player's score
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        """Increments the left player's score and updates the display."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increments the right player's score and updates the display."""
        self.r_score += 1
        self.update_scoreboard()