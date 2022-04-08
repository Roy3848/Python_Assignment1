# Concatenate two list in following:
final = []
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]


def match_list(which_list1, which_list2):
    for i in which_list1:  # iterating over the first list
        for j in which_list2:  # iterating over the second list
            # adding to the final list one after the other
            # index wise
            result = i + j
            final.append(result)
    return final


print(match_list(list1, list2))
