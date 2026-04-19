##################### Extra Hard Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas as pd
from pathlib import Path

LETTER_DIRECTORY = "letter_templates"
PLACEHOLDER = "[NAME]"
my_email = "test@gmail.com"
with open("C:/Users/jorda/python_mail.txt", "r") as f:
    password = f.readline()

now = dt.datetime.now()
# 1. Update the birthdays.csv
birthdays_df = pd.read_csv("birthdays.csv")
# birthdays_df['birthday_dt'] = pd.to_datetime(birthdays_df[['year','month','day']])

today_birthday = birthdays_df[(birthdays_df['day'] == now.day) & (birthdays_df['month'] == now.month)]

# 2. Check if today matches a birthday in the birthdays.csv
if not today_birthday.empty:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letter_templates = [p.name for p in Path(LETTER_DIRECTORY).iterdir() if p.is_file()]
    for index, person in today_birthday.iterrows():
        letter = random.choice(letter_templates)
        with open(f"{LETTER_DIRECTORY}/{letter}") as template_file:
            template_contents = template_file.read()
            email_msg = template_contents.replace(PLACEHOLDER, person['name'])
            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                # starts secure connection
                connection.starttls()
                connection.login(my_email, password)
                connection.sendmail(from_addr=my_email, to_addrs=person['email'], msg=email_msg)









