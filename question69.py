# Create a function that takes a string containing integers as well as other characters
# and return the sum of the negative integers only.
# Ex negative_sum("22 13%14&-11-22 13 12") => -11 + -22 = -33

import re
string_a = input("Enter any string with numbers and operations: ")


def negative_addition(string):
    total = 0
    for items in re.findall("-\d+", string):
            total = total + int(items)
    return total


print(negative_addition(string_a))
