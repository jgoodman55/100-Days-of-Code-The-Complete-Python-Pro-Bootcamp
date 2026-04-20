# Pong

A two-player Pong game built with Python's `turtle` module. Both players control paddles on opposite sides of the screen, rallying a ball back and forth. The ball speeds up with each successful hit, and a point is awarded whenever the ball gets past the opposing paddle.

---

## Gameplay

- Two players compete on the same keyboard
- The ball bounces off the top and bottom walls and off each paddle
- The ball speeds up slightly after every paddle hit
- A point is scored when the ball passes a paddle and exits the screen
- Scores are displayed at the top of the screen throughout the match

---

## Controls

| Action | Left Player | Right Player |
|---|---|---|
| Move up | `W` | `Up Arrow` |
| Move down | `S` | `Down Arrow` |

---

## Features

- Smooth ball movement with independent X and Y velocity components
- Progressive ball speed increase on each paddle bounce
- Paddle boundary restrictions to keep paddles within the screen
- Ball resets to center after each point, reversing direction toward the scoring player
- Live score display for both players

---

## Requirements

- Python 3.8 or higher
- No third-party dependencies (`turtle` is part of the Python standard library)

---

## Usage

```bash
python main.py
```

Click the window to exit.

---

## Project Structure

```
.
├── main.py         # Game loop, collision detection, and screen setup
├── ball.py         # Ball movement, bouncing, speed, and reset logic
├── paddle.py       # Paddle movement with boundary restrictions
└── scoreboard.py   # Score tracking and display
```

---

## Module Overview

**`main.py`** sets up an 800x600 black screen, initializes both paddles, the ball, and the scoreboard, then runs the game loop at 0.1s intervals. It handles wall bounces, paddle collisions, and point scoring.

**`ball.py`** defines the `Ball` class with separate `x_move` and `y_move` components. `bounce_x` and `bounce_y` reverse direction on collision. `increase_speed` nudges the X velocity by 2 pixels per paddle hit. `reset_position` returns the ball to center and reverses its horizontal direction.

**`paddle.py`** defines the `Paddle` class as a tall, narrow white rectangle. `up` and `down` move the paddle by 20 pixels per keypress and clamp movement at the top and bottom edges of the screen.

**`scoreboard.py`** tracks left and right scores independently, redraws both values on every update, and positions them symmetrically near the top of the screen.

---

## Constants at a Glance

| Constant | Value | Description |
|---|---|---|
| `MOVE_DISTANCE` (ball) | 10 | Initial ball speed in pixels per tick |
| Speed increment | 2 | Added to ball X speed per paddle bounce |
| Paddle move step | 20 | Pixels the paddle moves per keypress |
| Screen width | 800 | Horizontal play area |
| Screen height | 600 | Vertical play area |
| Paddle collision range | 50 | Distance threshold for paddle hit detection |
