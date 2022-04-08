# remove items from list, add items at specified index

numbers_list = [54, 44, 27, 79, 91, 41]


def modify_list():
    numbers_list.pop(2)  # to remove the items from the list
    numbers_list.pop(3)  # to remove the items from the list
    print(numbers_list)  # then print the list
    numbers_list.insert(2, 11)  # inset values at index 2
    numbers_list.append(11)  # add values with the append function, which add the element at the end of the list
    return numbers_list


print(modify_list())
