# Return the difference between largest and smallest number in the list

# Note: while finding the largest number we are taking 0 initially as a reference for the comparison with the
# other values of the list. Because we are searching for larger number and all the values are larger than 0.
# Note2: But while finding the smallest number we are taking any value from the list as reference to compare with the
# rest of the elements in the list. Why? Because 0 can't be use, cause less than 0 means all negative values, so we have
# to choose a number from the list as a reference

# that is the reason (in the case of taking output from the console) after the list is being created we are setting
# the lowest reference variable otherwise we get an error of Index.


# defining a function to get the difference between largest and smallest number
def largest_smallest_difference():
    list1 = []  # an empty list to store the values after appending
    i = 0  # set i is equal to 0 because i is reference for total elements to run the loop
    highest_number = 0  # highest_number variable is set to 0 because to set as reference for the rest of the
    # values in the list
    total_elements = int(input("Enter number of elements: "))  # ask the user to enter total number of elements
    while i < total_elements:  # while loop with a condition i < total_elements
        element = int(input("Enter element: "))  # then ask the user to enter elements
        list1.append(element)  # all the elements entered by the user have been appended in the list
        i = i + 1  # for every iteration the i reference variable is incremented by 1
    print(list1)  # print the final list
    lowest_number = list1[0]  # once the list is out, then we set the least reference variable to compare
    # with the rest of the values in the list.
    for j in list1:  # for the iteration in the list
        if j > highest_number:  # those many times the j is greater than the highest number then
            # that value will be stored in the highest_number variable.
            highest_number = j  # will be stored in the variable
    for x in list1:  # similarly, again iterating through the same list
        # but this time in the search of the smallest number
        if x < lowest_number:  # every time x is lower than the lowest number.
            lowest_number = x  # those many times the number will be stored in the lowest_number variable

# the final value of the highest_number variable and lowest_number variable
    return highest_number - lowest_number  # with that will be calculating the difference between them


# DRIVER CODE
# CALLING OUT THE FUNCTION
print(largest_smallest_difference())

