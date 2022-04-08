# Convert age to days

while True:  # to make an infinite loop
    try:  # try block to let the user enter only integer values
        age = int(input("Enter your age: "))  # to enter the input
        days = age * 365  # multiply with 365 to convert age to days
        print(days)  # print the result
        break  # break statement to end the infinite loop
    except ValueError:  # except value to catch the error when they enter string.
        print("Age can not be alphabets.")

print("This is the expected seconds.")
