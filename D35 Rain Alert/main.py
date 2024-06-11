import requests
from twilio.rest import Client
import os

OPEN_WEATHER_END = os.environ.get("OPEN_WEATHER_END")
OPEN_WEATHER_KEY = os.environ.get("OPEN_WEATHER_KEY")
TWILIO_KEY = os.environ.get("TWILIO_KEY")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
TWILIO_SID = os.environ.get("TWILIO_SID")

MY_LAT = os.environ.get("MY_LAT")
MY_LON = os.environ.get("MY_LON")
print(MY_LAT)

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "daily,minutely,current",
    "appid": OPEN_WEATHER_KEY
}

response = requests.get(OPEN_WEATHER_END, params=parameters)
response.raise_for_status()
weather_data = response.json()

rain = False
for hour in weather_data["hourly"][:16]:
    condition_id = hour["weather"][0]["id"]
    if condition_id < 700:
        rain = True

if rain:
    client = Client(TWILIO_SID, TWILIO_KEY)
    message = client.messages.create(
        to= "+12345432123",
        from_=TWILIO_PHONE,
        body="No motorcycle today"
    )
    print(message.status)
