# Find the largest number from the list
# Using for loop, while loop and conditional statements

# defining a function to find the largest number
def largest_number():
    list1 = []  # an empty list to store the values
    highest_number = 0  # highest number initially 0 to compare with all the values in the list
    i = 0  # i variable is a reference variable which is also set to 0 initially
    total_elements = int(input("Enter total elements: "))  # ask the user to enter number of elements in the list
    while i < total_elements:  # while loop to give condition to enter those many elements in the list till
        # the condition holds true.
        element = int(input("Enter element: "))  # asking the user to enter elements.
        list1.append(element)  # append all the elements in the list
        i = i + 1  # for every iteration the i value will be increasing by 1 because i is a reference.
    print(list1)  # print the final list after appending the elements
    for j in list1:  # for loop to iterate over list1
        if j > highest_number:  # now j is also a reference to get the largest number in the list
            highest_number = j  # and every time j is larger than the highest number that number
            # will be stored in the highest number variable
    return highest_number  # and finally the highest number will be returned as an output


print(largest_number())
