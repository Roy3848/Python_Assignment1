# write a program to sort the date by ascending and descending order

numbers_list = []  # an empty list to store the final list
total_elements = int(input("Enter number of elements: "))  # user input


def order_data(numbers):  # function which takes one argument numbers(list of dates)
    for i in range(0, total_elements):
        # in every iteration to ask the user to add element
        element = int(input("Enter elements: "))
        # and those elements will be appended in the numbers list
        numbers.append(element)

    print(numbers)

    order_ascending = sorted(numbers)  # sort the list in ascending order
    order_descending = sorted(numbers, reverse=True)  # sort the list in descending order
    print(order_ascending)
    print(order_descending)


order_data(numbers_list)

