# Compare two string by comparing count of characters
# METHOD 1 (using len() function)

def string_comparison(string1, string2):  # define a function for string comparison
    # to compare the count of characters, so use len() function
    if len(string1) == len(string2):  # conditional statement for the comparison based on the length funtion
        return True
    else:
        return False


print(string_comparison(input("Enter any string: "), input("Enter any string: ")))

# METHOD 2 (using for loop)
def string_comparison(string1, string2):
    total1 = 0
    total2 = 0
    # comparison of the count of characters using for loop (through iteration)
    for i in range(len(string1)):
        total1 = total1 + 1  # for every iteration the count is increasing by 1 and
        # getting stored in the total1 variable which was initially set to 0 for this purpose
    for j in range(len(string2)):
        total2 = total2 + 1  # the same case as of total1
    if total1 == total2:  # conditional statement to check of the count of the characters
        # by comparing the total values
        return True
    else:
        return False


print(string_comparison(input("Enter a string: "), input("Enter a string: ")))

# METHOD 3 (using while loop)


def string_comparison(string1, string2):
    total1 = 0
    total2 = 0
    i = 0
    j = 0
    # while loop functionality same like for loop,
    # but we need an extra variable for the reference purpose
    # and to build the condition for while loop
    while i < len(string1):
        total1 = total1 + 1  # for every iteration total1 variable will be increased by 1 and will be counting
        i = i + 1  # and also the i reference variable will also be increased by 1.
        # it means for every increment, the iteration is completing.
        # when the while loop condition does not hold anymore, then the iteration gets completed.
    while j < len(string2):  # same like the first while loop.
        total2 = total2 + 1
        j = j + 1
    if total1 == total2:
        return True
    else:
        return False


# calling out the function
print(string_comparison(input("Enter a string: "), input("Enter a string: ")))

