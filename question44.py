# Create a list by picking up odd index items from the first list
# and picking up even index items from the second list
# Approach one (Using index method)

odd_even = []
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]


def pick_odd_even(which_list1, which_list2):
    for i in which_list1:
        if which_list1.index(i) % 2 != 0:  # if odd index items  in the first
            odd_even.append(i)  # then append in the odd_even list

    for j in which_list2:
        if which_list2.index(j) % 2 == 0:  # if even items in the second list
            odd_even.append(j)  # then append in the odd_even list
    return odd_even


print(pick_odd_even(list1, list2))


# Approach two (Using range method)
# range function never goes with iterable directly
# but range function goes with the length of the iterable.
# it means range function goes with only integer values not string
# in for loop "i" is the index. so whenever we are using range the "i" works as an index
# so whenever we use range and print(i) it prints the index value.
# so if we want to print out the elements of the list of each character of the string
# then we have to write "list_name[index]"
# in this example "even_odd.append(list_name[index])"

even_odd = []


def pick_even_odd(where_list1, where_list2):
    for i in range(0, len(where_list1)):
        if i % 2 != 0:
            even_odd.append(i)

    for j in range(0, len(where_list2)):
        if j % 2 == 0:
            even_odd.append(j)

    return even_odd


print(pick_even_odd(list1, list2))
