import requests
from twilio.rest import Client
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_KEY = os.environ.get("ALPHA_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")
TWILIO_KEY = os.environ.get("TWILIO_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_PHONE = os.environ.get("TWILIO_PHONE")
TARGET_PHONE = os.environ.get("TARGET_PHONE")

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then Get News.

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_KEY,
}

alpha_response = requests.get("https://www.alphavantage.co/query", params=alpha_parameters)
alpha_response.raise_for_status()
alpha_data = alpha_response.json()["Time Series (Daily)"]
alpha_list = [value for (key, value) in alpha_data.items()]

yesterday_close = float(alpha_list[0]["4. close"])
previous_day_close = float(alpha_list[1]["4. close"])
print(f"{yesterday_close}")
print(f"{previous_day_close}")

percent_change = round(1 - (previous_day_close / yesterday_close), 3) * 100

print(percent_change)
percent_text = ""
if percent_change >= 0:
    percent_text = f"🔺{percent_change}%"
elif percent_change < 0:
    percent_text = f"🔻{percent_change*-1}%"

# STEP 2: Use https://newsapi.org
# get the first 3 news pieces for the COMPANY_NAME.

if -5 > percent_change > 5:
    news_parameters = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "apiKey": NEWS_KEY
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()

    client = Client(TWILIO_SID, TWILIO_KEY)
    for i in range(3):
        news_data = news_response.json()["articles"][i]
        print(f"Headline: {news_data['title']}")

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
        message = client.messages.create(
            to=TARGET_PHONE,
            from_=TWILIO_PHONE,
            body=f"{COMPANY_NAME} {percent_text}\n\n"
                 f"Headline: {news_data['title']}\n\n"
                 f"Brief: {news_data['description']}\n\n"
                 f"Link: {news_data['url']}"
        )
