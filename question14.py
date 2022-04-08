# check if obj1 is equal to obj2

list1 = [2, 3, 4, 5]  # list1 is object 1
list2 = [2, 3, 4]  # list2 is object2

# defining a function to compare two objects
def compare_object(obj1, obj2):
    # to check if both the objects are equal or not
    if obj1 == obj2:
        return True
    else:
        return False


print(compare_object(list1, list2))
