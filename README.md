# Py-Day22

# The Pong Game  clásic

This project is a complete implementation of the classic arcade game, Pong, built using Python's `turtle` module. It's a two-player game featuring score tracking, increasing ball speed, and responsive paddle controls.

-----

## Features 🌟

  * **Two-Player Gameplay**: Control the left paddle with the 'W' and 'S' keys and the right paddle with the 'Up' and 'Down' arrow keys.
  * **Score Tracking**: The scoreboard at the top of the screen keeps track of each player's score.
  * **Increasing Difficulty**: The ball's speed increases every time it's hit by a paddle, making the game more challenging as the rally continues.
  * **Object-Oriented Design**: The code is cleanly organized into separate classes for the paddles, ball, and scoreboard, making it easy to read and maintain.

-----

## How to Play 🎮

The objective is to score points by getting the ball past your opponent's paddle.

  * **Left Player**:
      * Move Up: `W`
      * Move Down: `S`
  * **Right Player**:
      * Move Up: `Up Arrow`
      * Move Down: `Down Arrow`

The game continues until one player reaches the winning score. (There is no winning score.)

-----

## Project Structure 📂

The project is broken down into four main Python files:

  * `pong-game.py`: This is the main file that initializes the screen and runs the game loop.
  * `paddle.py`: Contains the `Paddle` class, which defines the behavior and appearance of the player paddles.
  * `ball.py`: Contains the `Ball` class, which manages the ball's movement, speed, and collision physics.
  * `scoreboard.py`: Contains the `Scoreboard` class for displaying and updating the score.

-----

## Getting Started 🚀

To run this game, you just need to have Python 3 installed on your system. The `turtle` module is part of the standard library, so no additional installations are required.

1.  **Clone the repository or download the files** into a single directory.
2.  **Open your terminal or command prompt** and navigate to that directory.
3.  **Run the game** with the following command:
    ```bash
    python pong-game.py
    ```

Enjoy the game!
