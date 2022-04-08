# Write a function to compute 5/0 and use try/except to catch the exceptions.

try:  # try block to try the division by 0
    print(5/0)
except ZeroDivisionError:  # but as this will raise an error so will catch by exception block
    # and the below message will be printed.
    print("This division is not possible'\n'because dividing by zero gives undefined")
