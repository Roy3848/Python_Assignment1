# Concat two list index wise
# Method 1 (using zip function with for loop)
# zip function takes iterable and returns a single iterator.
# In this case zip function is concatenating the string and return into a single list and return list.\

result_lst = []
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


def index_wise(which_list1, which_list2):
    for i, j in zip(which_list1, which_list2):  # iterating over both the list index wise
        result = i + j  # concatenating both the list index wise
        result_lst.append(result)  # and appending in the new list
    return result_lst


print(index_wise(list1, list2))

# Method 2 (using list comprehension and zip function)
# the same logic as of above but using list comprehension
result_list = [i + j for i, j in zip(list1, list2)]
print(result_list)


un_list = ["Sayak", "i", "th", "be"]
un_list1 = ["Roy", "s", "e", "st"]

print("The first list is: " + str(un_list))
print('The second list is: ' + str(un_list1))

final_result = [i + j for i, j in zip(un_list, un_list1)]
print(final_result)
