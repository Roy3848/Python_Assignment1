# Convert string into integer

while True:  # to make an infinite loop
    # in string, we can add anything whether numbers or alphabets,
    # so it is out of the try block
    # because it will not raise an error.
    input_something = input("Enter (any word or number): ")  # to input any string
    try:  # try block to convert the string into integer
        # variable to store the type converted value of the input_something variable
        input1 = int(input_something)
        # to check the type of the variable
        print(type(input1))
        break  # break statement to end the infinite loop after finding expected result
    except ValueError:  # exception if they enter alphabets then will not get converted into integers
        # because alphabets can never be integers.
        print(input_something)
        print(type(input_something))
        print("No Change, Because alphabets cant be changed into integers")
print("Been successfully changed from string to integer.")

# Convert integer into string
while True:  # to make the infinite loop
    try:  # try block to let the user enter a string value
        input_something = int(input("Enter (any number): "))
        # another variable to store the string converted value in it.
        input1 = str(input_something)
        # Now check the type of the new variable./
        print(type(input1))
        break  # to  end the infinite loop
    except ValueError:  # exception is for if the user enter wrong values, they get a prompt message in the console
        print("Invalid Entry.")
print("Been successfully changed from integer to string.")
