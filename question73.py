# Create a function that takes two dates and returns the number of days between the first and second date.
import datetime

date1 = input("Enter one date: ")  # asking the user to enter the first date
date2 = input("Enter another date: ")  # asking the user to enter the second date


# function which takes two arguments, the first argument is first date
# and the second arguments is the second date from which the first will get subtracted
def date_difference(which_day1, which_day2):
    first_date = datetime.datetime.strptime(which_day1, "%d-%m-%Y")  # strptime function to format date input by user
    second_date = datetime.datetime.strptime(which_day2, "%d-%m-%Y")  # strptime function to format date input by user
    return (second_date - first_date).days  # .days function returns the number of days in between this two dates


# calling out the function
print(date_difference(date1, date2))
