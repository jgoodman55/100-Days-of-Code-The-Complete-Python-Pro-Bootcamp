# Turtle Crossing

A Frogger-inspired arcade game built with Python's `turtle` module. Guide your turtle safely across a busy road of oncoming cars, advancing through increasingly difficult levels as the traffic speeds up with each crossing.

---

## Gameplay

- Move your turtle up the screen using the **Up arrow key**
- Avoid the oncoming cars moving from right to left
- Reach the finish line at the top to advance to the next level
- Each level increases car speed
- The game ends on collision with a car

---

## Features

- Randomly colored cars spawned at varied vertical positions
- Progressive difficulty with speed increasing per level
- Live level counter displayed on screen
- Collision detection between the player and cars
- Off-screen car recycling to maintain a continuous traffic flow
- "Game Over" message displayed on collision

---

## Requirements

- Python 3.8 or higher
- No third-party dependencies (`turtle` is part of the Python standard library)

---

## Usage

```bash
python main.py
```

Click the window to exit after the game ends.

---

## Project Structure

```
.
├── main.py           # Game loop, collision detection, and screen setup
├── player.py         # Player movement, position reset, and finish line detection
├── car_manager.py    # Car spawning, movement, and speed management
└── scoreboard.py     # Level display and game over message
```

---

## Module Overview

**`main.py`** initializes the screen and all game objects, runs the game loop at 0.1s intervals, and handles finish line crossing, car recycling, and collision detection.

**`player.py`** defines the `Player` class (a `Turtle` subclass) that starts at the bottom center, moves upward on keypress, resets position after each crossing, and detects when the finish line is reached.

**`car_manager.py`** manages a list of car `Turtle` objects, initializes 30 cars at random positions on startup, spawns replacement cars from the right edge when existing cars exit the left edge, and increases movement speed on each level up.

**`scoreboard.py`** tracks and displays the current level in the top-left corner and writes a centered "Game Over" message when the player collides with a car.

---

## Constants at a Glance

| Constant | Value | Description |
|---|---|---|
| `STARTING_MOVE_DISTANCE` | 5 | Initial car speed (pixels per tick) |
| `MOVE_INCREMENT` | 10 | Speed increase per level |
| `STARTING_X_POSITION` | 300 | X position where new cars spawn |
| `MOVE_DISTANCE` (player) | 10 | Pixels the player moves per keypress |
| `FINISH_LINE_Y` | 280 | Y coordinate of the finish line |
