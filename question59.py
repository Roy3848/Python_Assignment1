# Merge two dictionary into one and rename the dictionary keywords.
# Method 1 (using | to merge two dictionaries.)
dict1 = {"fname": "Sayak", "lname": "Roy"}
dict2 = {"address": "Kolkata", "PIN": 700110}


def merge_dict(which_dict1, which_dict2):
    result = which_dict1 | which_dict2
    return result


dict3 = merge_dict(dict1, dict2)
print(dict3)


# Method 2 (using update function)

def merge_dict1(which_dict3, which_dict4):
    return which_dict3.update(which_dict4)


print(merge_dict1(dict1, dict2))  # this return none
print(dict1)


# Method 3 (using ** method)

def merge_dict2(which_dict5, which_dict6):
    return {**which_dict5, **which_dict6}


dict4 = merge_dict2(dict1, dict2)
print(dict4)
