# Snake Game

A classic Snake game built with Python's `turtle` module. Guide the snake to eat food, grow longer, and rack up points. The high score persists between sessions via a local text file, and the game resets automatically on collision rather than closing.

---

## Features

- Smooth snake movement with segment-following locomotion
- Arrow key controls with reverse-direction prevention
- Food spawns at a random position each time it is eaten
- Score increments on every food pickup
- High score persists to disk and survives between sessions
- Wall and self-collision trigger an automatic reset instead of ending the game
- Snake segments are moved off-screen on reset to avoid visual artifacts

---

## Requirements

- Python 3.8 or higher
- No third-party dependencies (`turtle` is part of the Python standard library)
- A `data.txt` file containing a single integer (e.g. `0`) must exist in the working directory before the first run

---

## Setup

Create the high score file before running for the first time:

```bash
echo 0 > data.txt
```

Then start the game:

```bash
python main.py
```

---

## Controls

| Key | Action |
|---|---|
| `Up Arrow` | Move up |
| `Down Arrow` | Move down |
| `Left Arrow` | Move left |
| `Right Arrow` | Move right |

The snake cannot reverse directly into itself; opposite-direction inputs are ignored.

---

## Project Structure

```
.
├── main.py          # Game loop, collision detection, and screen setup
├── snake.py         # Snake construction, movement, extension, and reset
├── food.py          # Food placement at random coordinates
├── scoreboard.py    # Score display, high score tracking, and file persistence
└── data.txt         # Stores the all-time high score as a plain integer
```

---

## Module Overview

**`main.py`** sets up a 600x600 black screen and runs the game loop at 0.1s intervals. It detects food collisions within 15 pixels, wall collisions at the 280-pixel boundary, and self-collisions between the head and any non-head segment within 10 pixels. On any collision, both the snake and scoreboard are reset.

**`snake.py`** builds the snake from three starting segments at fixed positions. Each move shifts every segment to the position of the one ahead of it, then advances the head forward. `extend` adds a new segment at the tail's current position. `reset` teleports all existing segments off-screen before rebuilding from scratch.

**`food.py`** is a small `Turtle` subclass that spawns as a half-size blue circle. `refresh` moves it to a new random position within the play area each time it is eaten.

**`scoreboard.py`** reads the high score from `data.txt` on initialization. `refresh_score` increments and redraws the display. `reset` compares the current score to the high score, writes a new high score to disk if it has been beaten, then resets the current score to zero.
