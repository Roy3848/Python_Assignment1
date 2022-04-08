# returns the next number from the integer passed
# METHOD 1 (with function)
# defining a function to get the number argument
def next_number(number):
    return number + 1  # once we get the number then add 1 to it to get the next number


# calling the function
print(next_number(int(input("Enter any number: "))))


# METHOD 2 (using while loop for infinite loop)
def next_integer():
    while True:  # this is to make infinite loop
        fav_number = int(input("Enter a number: "))  # Enter the number
        number_next = fav_number + 1  # then add 1 to it, to get the next number.
        # Get the output. The final result.
        print("The next integer rof the number passed is {}.".format(number_next))


# calling out the function
next_integer()
