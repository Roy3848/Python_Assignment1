# Reverse the tuple
# Method 1 (using slicing)
numbers_tuple = (45, 54, 23, 12, 2, 9)


def reverse_tuple(numbers):
    return numbers[::-1]  # slicing the tuple to reverse


print(reverse_tuple(numbers_tuple))


# Method 2 (using for loop + function)
# converting the tuple into list
# and performing append function and again converting the list back to tuple
list1 = []


def reverse_tuple():
    elements_count = int(input("Enter the total number of elements: "))
    for i in range(1, elements_count+1):
        element = int(input("Enter elements: "))
        list1.append(element)  # the elements entered by the user added to the list
    tuple1 = list1[::-1]  # converting the list into tuple
    return tuple1  # getting the final tuple as expected


print(reverse_tuple())
