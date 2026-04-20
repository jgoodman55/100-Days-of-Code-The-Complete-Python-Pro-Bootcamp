# Workout Tracker

A Python script that accepts a plain-English description of a workout, uses the Nutritionix API to parse and calculate exercise details, and logs each exercise automatically to a Google Sheet via the Sheety API. Each row is stamped with the current date, time, exercise name, duration, and calories burned.

---

## Features

- Natural language exercise input (e.g. "ran 5k and did 30 minutes of cycling")
- Nutritionix API interprets the text and returns structured exercise data
- Calories and duration calculated based on personal profile (gender, weight, height, age)
- Each exercise logged as a separate row in a Google Sheet
- Credentials and tokens loaded from a `.env` file

---

## Requirements

- Python 3.8 or higher

Install dependencies:

```bash
pip install requests python-dotenv
```

---

## Setup

### 1. Nutritionix API

Sign up at [nutritionix.com](https://www.nutritionix.com/business/api) to get an `APP_ID` and `API_KEY`.

### 2. Sheety API

1. Create a Google Sheet with the following column headers in row 1:

   `date`, `time`, `exercise`, `duration`, `calories`

2. Connect it to [sheety.co](https://sheety.co) and enable POST requests
3. Generate a Bearer token under the project's authentication settings
4. Note your Sheety endpoint username, project name, and sheet name

### 3. Environment Variables

Create a `.env` file in the same directory as `main.py`:

```
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
BEARER_TOKEN=your_sheety_bearer_token
```

### 4. Personal Profile

Update the constants near the top of `main.py` to match your profile so calorie calculations are accurate:

```python
GENDER     = "male"
WEIGHT_KG  = 75
HEIGHT_CM  = 163
AGE        = 29
```

### 5. Sheety Identifiers

Update these three constants to match your Sheety project:

```python
USERNAME     = "your_sheety_username"
PROJECT_NAME = "your_project_name"
SHEET_NAME   = "your_sheet_name"
```

---

## Usage

```bash
python main.py
```

When prompted, type a description of your workout in plain English:

```
Tell me which exercises you did: ran for 20 minutes and did 15 minutes of yoga
```

The script will log each exercise to your Google Sheet and print the Sheety API response for each row.

---

## Example Sheet Output

| date | time | exercise | duration | calories |
|---|---|---|---|---|
| 19/04/2026 | 18:32:10 | Running | 20 | 218.5 |
| 19/04/2026 | 18:32:11 | Yoga | 15 | 52.3 |

---

## Notes

- Never commit your `.env` file. Add it to `.gitignore` to keep credentials out of version control.
- The Sheety free tier has rate limits. Logging many exercises in rapid succession may trigger them.
- Exercise names are title-cased before being written to the sheet.
