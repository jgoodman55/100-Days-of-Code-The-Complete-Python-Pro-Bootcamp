import smtplib
import datetime as dt
import random

my_email = "test@gmail.com"
with open("C:/Users/jorda/python_mail.txt", "r") as f:
    password = f.readline()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt","r") as quotes_file:
        quotes = quotes_file.readlines()
        quote_of_the_day = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        # starts secure connection
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs="test@gmail.com", msg=quote_of_the_day)


