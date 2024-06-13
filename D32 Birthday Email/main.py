import datetime as dt
import smtplib
import random as r
import pandas as pa
MY_EMAIL = "my_email@gmail.com"
MY_PASSWORD = "My_Password123"


now = dt.datetime.now()
today = (now.month, now.day)

birthdays = {(row.month, row.day):row
             for (index, row) in pa.read_csv("birthdays.csv").iterrows()}

if today in birthdays:
    with open(f"letter_templates/letter_{r.randint(1, 3)}.txt") as letter:
        email_contents = letter.read().replace("[NAME]", birthdays[today]['name'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthdays[today]['email'],
            msg=f"Subject:Happy Birthday!\n\n"
                f"{email_contents}"
        )


print(email_contents)

