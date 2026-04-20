# Quizzler

A True/False trivia quiz app with a Tkinter GUI. Questions are fetched live from the Open Trivia Database API and presented one at a time. The canvas flashes green or red after each answer, and the score updates in real time until all questions are exhausted.

---

## Features

- Fetches 10 fresh True/False questions from the Open Trivia DB on each run
- Decodes HTML entities in question text so special characters display correctly
- Green and red canvas feedback after each answer with a 1-second delay before advancing
- Live score display updated after every question
- True and False buttons disabled automatically when the quiz ends
- Clean separation of data, logic, and UI across dedicated modules

---

## Requirements

- Python 3.8 or higher
- Tkinter (included with most Python installations)

Install the one third-party dependency:

```bash
pip install requests
```

---

## Project Structure

```
.
├── main.py             # Entry point: builds the question bank and launches the UI
├── data.py             # Fetches questions from the Open Trivia DB API
├── question_model.py   # Question dataclass holding text and correct answer
├── quiz_brain.py       # Quiz state: question progression and answer checking
├── ui.py               # Tkinter GUI: canvas, buttons, score label, and feedback
└── images/
    ├── true.png        # Image for the True button
    └── false.png       # Image for the False button
```

---

## Usage

```bash
python main.py
```

A window will open with the first question displayed on the canvas. Click the True or False button to answer. The canvas turns green for a correct answer and red for an incorrect one, then advances to the next question after one second. Your score is shown in the top-right corner throughout.

---

## API Configuration

Questions are pulled from the [Open Trivia Database](https://opentdb.com/). The default request in `data.py` fetches:

| Parameter | Value | Description |
|---|---|---|
| `amount` | 10 | Number of questions per session |
| `type` | boolean | True/False questions only |
| `category` | 18 | Science: Computers |

To change the category or difficulty, update the `parameters` dictionary in `data.py`. A full list of category IDs is available at [opentdb.com/api_config.php](https://opentdb.com/api_config.php).

---

## Module Overview

**`data.py`** makes a GET request to the Open Trivia DB, raises an error on a bad response, and exposes the results list as `question_data`.

**`question_model.py`** defines a minimal `Question` class holding `text` and `answer` attributes.

**`quiz_brain.py`** manages the current question index and score, advances through the question list, unescapes HTML entities with `html.unescape`, and checks answers case-insensitively.

**`ui.py`** builds the Tkinter window with a score label, a canvas for question text, and image buttons for True and False. It calls `give_feedback` on each answer to flash the canvas color, then schedules `get_next_question` after 1 second using `window.after`.
