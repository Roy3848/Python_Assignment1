# Modify a tuple

# function to convert the tuple into list
# then modify the list
# and then convert the list back into tuple
def modify_tuple():
    tuple1 = (2, 3, 4, 5, 6)
    list1 = list(tuple1)
    list1.append(34)
    tuple1 = tuple(list1)
    return tuple1


print(modify_tuple())

# method 2

tuple3 = (4, 5, 6, 8, 9)
list2 = list(tuple3)
list2[1] = 45
tuple3 = tuple(list2)
print(tuple3)


