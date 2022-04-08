# create a function that takes list and string.
# the function should remove the letters in the string from the list and return the list

# using remove() function

any_string = input("Enter any string: ").lower()
any_list = ["g", "u", "d", "i", "s", "y", "a", "k", "o", "p", "u"]


def string_list(list1, string1):
    removed_elements = []
    for i in string1:
        if i in list1:
            list1.remove(i)
            removed_elements.append(i)
    return removed_elements


print("Removed elements list:", string_list(any_list, any_string))
print("This are the remaining elements in the main list:", any_list)
