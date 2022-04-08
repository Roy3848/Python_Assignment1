# How to convert hours into seconds.

while True:  # to make an infinite loop
    try:  # try block to let the user enter only integer values
        hours = int(input("Enter Hours: "))  # to enter the input
        if 0 <= int(hours) <= 23:  # if hours between 0 and 23
            # then this will be played
            hours = hours * 3600
            print(hours)
            break  # break statement to end the infinite loop
        else:  # if hours not between 0 and 23
            # then these statements will be played
            print("Enter a valid hour.")
    except ValueError:  # except value to catch the error when they enter string.
        print("Hours can not be alphabets.")

print("This is the expected seconds.")
