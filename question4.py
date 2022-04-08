# Return the remainder of two numbers:

while True:  # to create an infinite loop
    number1 = input("Enter Number1: ")  # variable to enter a number
    number2 = input("Enter Number2: ")  # another variable to enter another number
    try:  # try to make sure the user entering integer values both the values
        print("The sum of these two numbers are:", abs(int(number1) % int(number2)))
        break  # break statement to end the infinite loop.
    except ValueError:  # if any error then it will come the exception part.
        print("The calculation will not be possible.")
