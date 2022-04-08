# Get the sum of all list elements
# METHOD 1 (using for loop)
list1 = [45, 35, 25, 15, 65, 55]  # variable to store the list


def addition(numbers):  # define function for the addition
    total = 0  # initially calling a variable and set to 0 because to store the final result in the same variable
    for i in range(0, len(numbers)):  # iterating through the range of the total length of the list.
        total = total + numbers[i]  # and in every iteration add the numbers and store in the total variable
        # which was set to 0 initially
    return total  # return the final result


# calling out the function
print(addition(list1))

# METHOD 2 (using while loop)

list2 = [45, 35, 25, 15, 65, 55]


def addition1(numbers):
    total = 0  # initially total is 0
    i = 0    # index starts at 0
    while i < len(numbers):  # while loop with the condition
        ###################################################
        # till i is less than the length of the list
        # the numbers will be adding one after the other with the total variable
        # and get stored in the total variable
        ##################################################
        total = total + numbers[i]
        i = i + 1  # and in every iteration the i value increases by 1 to keep the
    return total


print(addition1(list2))

# METHOD 3 (using sum() function)
list3 = [45, 35, 25, 15, 65, 55]


def addition2(numbers):
    # using sum function to add all the numbers
    return sum(numbers)


# calling out the function
print(addition2(list3))
