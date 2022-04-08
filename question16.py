# Find the smallest number from the list
# Using for loop, while loop and conditional statements

# defining a function to find the smallest number
def smallest_number():
    list1 = []  # an empty list to store the values
    i = 0  # i variable is a reference variable for total_elements comparison, which is also set to 0 initially
    total_elements = int(input("Enter total elements: "))  # ask the user to enter number of elements in the list
    while i < total_elements:  # while loop to give condition to enter those many elements in the list till
        # the condition holds true.
        element = int(input("Enter element: "))  # asking the user to enter elements.
        list1.append(element)  # append all the elements in the list
        i = i + 1  # for every iteration the i value will be increase by 1 because i is a reference.
    print(list1)  # print the final list after appending the elements
    lowest_number = list1[0]  # this is also for reference with the comparison with other elements in the list
    for j in list1:  # for loop to iterate over list1
        if j < lowest_number:  # now j is also a reference to get the lowest number in the list
            lowest_number = j  # and every time j is smaller than the lowest number that number
            # will be stored in the lowest number variable
    return lowest_number  # and finally the lowest number will be returned as an output


print(smallest_number())
