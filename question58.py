# Convert list into dictionary
# Method 1 (using dict comprehension)
list1 = ["fname", "Sayak", "lname", "Roy", "Address", "kolkata", "phone", 6589034]


def dict_conversion(alist):
    result_dict = {alist[i]: alist[i + 1] for i in range(0, len(alist), 2)}
    return result_dict


print(dict_conversion(list1))
