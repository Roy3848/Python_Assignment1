# write a program to print a list after removing 0th, 4th and 5th elements from the list

# Method 1 (using enumerate function and for loop)
#                0   1   2   3   4   5
numbers_list = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1]
changed_list = []

for index, value in enumerate(numbers_list):
    if index not in (0, 4, 5):
        changed_list.append(value)

print(changed_list)

# Method 2 (using enumerate function and list comprehension)

print("\nUsing List Comprehension")
changed_list1 = [value for index, value in enumerate(numbers_list) if index not in (0, 4, 5)]
print(changed_list1)