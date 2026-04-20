# U.S. States Game

An interactive geography quiz built with Python's `turtle` module and pandas. A blank map of the United States is displayed on screen, and the player types state names one at a time. Each correct guess is written directly onto the map at the state's coordinates. Any states not guessed before exiting are saved to a CSV for later study.

---

## Features

- Blank U.S. map rendered as a turtle shape for a clean visual canvas
- Input prompt updates after each correct guess to show current progress
- Correct state names are written at their geographic coordinates on the map
- Case-insensitive matching via `.title()` normalization
- Typing "Exit" ends the game early without requiring all 50 states
- Missed states are exported to `states_to_learn.csv` automatically on exit

---

## Requirements

- Python 3.8 or higher
- The following files must be present in the same directory as `main.py`:

| File | Description |
|---|---|
| `blank_states_img.gif` | Blank U.S. map in GIF format for the turtle canvas |
| `50_states.csv` | CSV with columns: `state`, `x`, `y` (map coordinates) |

Install the one third-party dependency:

```bash
pip install pandas
```

---

## Usage

```bash
python main.py
```

A window will open showing the blank U.S. map. Type a state name into the prompt and press Enter. Correct guesses appear on the map. Type `Exit` at any point to end the session and generate the study file.

---

## Output

When the game ends (either by guessing all 50 states or typing "Exit"), a file named `states_to_learn.csv` is written to the working directory containing the names of all states that were not guessed. This file can be used as a flashcard list for a follow-up study session.

---

## Project Structure

```
.
├── main.py                  # Game logic and turtle rendering
├── blank_states_img.gif     # Map image used as the turtle canvas background
├── 50_states.csv            # State names and their x/y map coordinates
└── states_to_learn.csv      # Generated on exit with unguessed states
```

---

## How It Works

1. Loads the blank map GIF as a turtle shape and sets it as the screen background
2. Reads `50_states.csv` into a pandas DataFrame containing each state's name and pixel coordinates
3. Opens a text input prompt on each iteration, normalizing the entry with `.title()`
4. Filters the DataFrame for a matching state name
5. If a match is found, moves a hidden turtle to the state's coordinates and writes the name
6. On exit, filters out all guessed states and saves the remainder to `states_to_learn.csv`
