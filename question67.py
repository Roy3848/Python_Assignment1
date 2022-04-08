# Given the month and year as numbers, return whether that month contains a friday 13th

import datetime

month = int(input("Enter a month in numbers: "))
year = int(input("Enter any year: "))

time_date = "13/{}/{}".format(month, year)
format_data = "%d/%m/%Y"
if datetime.datetime.strptime(time_date, format_data).weekday() == 4:
    print("Yes this month contains a friday on 13th.")
else:
    print("NO.")
