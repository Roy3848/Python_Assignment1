# Find the day of the week from the given date, date get the input from the user

import datetime
import calendar


def which_day(date):
    # strptime function is used to set the format of the date,
    fav_day = datetime.datetime.strptime(date, "%d %m %Y").weekday()  # .weekday() function to get the name of the day.
    return calendar.day_name[fav_day]  # calendar.day_name also returns the name of the day


input_date = input("Enter your favourite date: ")
print(which_day(input_date))
