import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()
GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 163
AGE = 29

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

USERNAME = "f82eb4028ff1c61a85bec1c19edcfe28"
PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"

base_endpoint = "https://app.100daysofpython.dev"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

natural_exercise_endpoint = f"{base_endpoint}/v1/nutrition/natural/exercise"

BEARER_TOKEN = os.getenv("BEARER_TOKEN")

sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(natural_exercise_endpoint, json=parameters, headers=headers)
result = response.json().get("exercises")
print(result)

sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

today = dt.datetime.now()
formatted_date = today.strftime("%d/%m/%Y")
formatted_time = today.strftime("%X")

for exercise in result:
    body = {
      "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": exercise.get("name").title(),
        "duration": exercise.get("duration_min"),
        "calories": exercise.get("nf_calories")
      }
    }

    sheety_response = requests.post(sheety_endpoint, json=body, headers=sheety_headers)
    print(sheety_response.json())