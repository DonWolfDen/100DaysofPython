import requests
import pandas
from datetime import datetime
import smtplib
import time

MY_LAT = 38.8977, 
MY_LONG = -77.0365
MY_EMAIL = "my_email@gmail.com"
MY_PASS = "My_Password123"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_long = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat":MY_LAT,
        "long":MY_LONG,
        "formatted":0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    pandas.DataFrame(data).to_json("sun.json")
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = datetime.now()

    if sunrise >= now.hour or now.hour >= sunset:
        return True

while True:
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS IS OVERHEAD NOW\n\n"
                    "Look up. The International Space Station is flying over your house")

    time.sleep(60)