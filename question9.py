# Return the first element in a list
# METHOD 1 (using functions and without slicing)

friends = ["Maulik", "Sambhav", "Raju", "Kalu"]


def first_element(friends_list):
    return friends_list[0]  # just index number to access


print(first_element(friends))

# METHOD 2 (using functions and with slicing [start:stop:step])

def first_element1(friends1_list):
    return friends1_list[:1:]  # using slicing


print(first_element1(friends))

