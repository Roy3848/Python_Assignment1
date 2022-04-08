# Sort tuple by second item
# Method 1 (Using sort function)
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))


def sort_tuple(tup):
    list1 = list(tup)
    # we use lambda function when we require a nameless function for a short period of time
    list1.sort(key=lambda x: x[1])
    tup = tuple(list1)
    return tup


print(sort_tuple(tuple1))


# Method 2 (using sorted function)

def tuple_sort(tup1):
    # lambda can have many arguments but only one expression
    return sorted(tup1, key=lambda y: y[1])


print(tuple_sort(tuple1))
