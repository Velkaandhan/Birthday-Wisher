##################### Extra Hard Starting Project ######################
import csv
import datetime as dt
import random
import smtplib
import os
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
text_file = ["letter_templates\letter_1.txt","letter_templates\letter_2.txt","letter_templates\letter_3.txt"]
date = dt.datetime.now()
current_month = date.month
current_day = date.day

with open("birthdays.csv", 'r') as file:
    lines = csv.reader(file)
    next(lines)
    for each_line in lines :
        month = int(each_line[3])
        day = int(each_line[4])
        if month == current_month and day == current_day :
            selected_file = random.choice(text_file)
            with open(selected_file,'r') as content:
                content = content.read()
                name = each_line[0]
                birthday = each_line[0]
                modified_content = content.replace("[NAME]", name)
            to_email = each_line[1]
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject: Happy Birthday\n\n{modified_content}")
