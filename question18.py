# Concatenate two list of integers
# To concatenate two lists, first using for loop to traverse through the second list
# and then using append function to add all the values of the second list in the first list.

list1 = [23, 12, 45, 33]  # list1 variable for one list
list2 = [32, 54, 21, 34]  # list2 variable for another list

# to concatenate two list using for loop and append function
# for loop to iterate through the list we want to add after.
# append function to add all the values of the next list to the first list
for x in list2:
    list1.append(x)

print("The final Concatenated list:", list1)
