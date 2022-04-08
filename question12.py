# Convert hours and minutes into seconds

while True:  # to make an infinite loop
    hours = input("Enter Hours: ")  # variable to enter hours
    minutes = input("Enter minutes: ")  # variable to enter minutes
    try:  # try block to let the user enter valid hours and minutes
        hours = int(hours) * 3600  # calculation for converting hours into seconds
        minutes = int(minutes) * 60  # calculation for converting minutes into seconds
        print(int(hours) + int(minutes))  # hours and minutes both summoned up together
        break  # break statement to end the infinite loop once the result is found.
    except ValueError:  # exception if the user make a valueError while entering the values
        print("An error occurred while entering the hours and minutes.")  # print the following statement


print("THis is the expected seconds.")
