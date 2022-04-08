# Create a function that takes number and returns its length
# (use of len() function is prohibited.)
# Method by conversion from int to str
number = int(input("Enter any number: "))


def numbers_length(number1):
    num = str(number1)
    total_length = 0
    for i in num:
        total_length = total_length + 1
    return total_length


print(numbers_length(number))


# Method 2 (No conversion)

numbers1 = input("Enter any number: ")


def number_length1(num1):
    total_length1 = 0
    for j in num1:
        total_length1 = total_length1 + 1
    return total_length1


print(number_length1(numbers1))
