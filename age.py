# Script to find age from certain date using datetime
# Author: George Downer 07/10/2025

from datetime import date


def how_long_ago(inputted_date):
    # extract information from user input
    day, month, year = inputted_date.split("-")
    difference = date.today() - date(int(year), int(month), int(day)
                                     )  # find the difference in time (days)
    return difference.days // 365  # convert the days into years passed (age)


print(how_long_ago(input("Enter a string in the format 'day-month-year': ")))
