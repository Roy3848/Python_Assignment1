# Write a program to square each odd number

# variable to store a list of numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
odd_numbers = []  # an empty list to store the final result


def odd_square(numbers):  # function which takes one argument numbers (which is the list of numbers)
    for number in numbers:
        if number % 2 != 0:  # to check odd numbers
            number = number * number  # if odd numbers then make it squares
            odd_numbers.append(number)  # append in the odd_numbers list
    return odd_numbers


print(odd_square(numbers_list))
