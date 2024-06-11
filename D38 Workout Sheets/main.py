import requests
import os
from datetime import datetime

NUTRIX_ID = os.environ.get("NUTRIX_ID")
NUTRIX_KEY = os.environ.get("NUTRIX_KSHEETY_WORKOUTS_END = os.environ.get("SHEETY_END")
NUTRIX_EXERCISE_END = os.environ.get("NUTRIX_EXERCISE_END")

nutrix_headers = {
    "x-app-id": NUTRIX_ID,
    "x-app-key": NUTRIX_KEY,
}

nutrix_params = {
    "query": input("What exercises did you do today? "),
    "gender": "male",
    "weight_kg": 105,
    "height_cm": 180,
    "age": 25
}

nutrix_response = requests.post(url=NUTRIX_EXERCISE_END, headers=nutrix_headers, json=nutrix_params)
nutrix_response.raise_for_status()
nutrix_data = nutrix_response.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in nutrix_data["exercises"]:
    new_row = {
        "workouts": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    print(new_row)

    sheety_response = requests.post(url=SHEETY_WORKOUTS_END, json=new_row)
    sheety_response.raise_for_status()
    print(sheety_response.text)
