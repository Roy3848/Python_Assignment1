# Return the last element of the list

# variable to store the list
sample_list = ["maulik", "sambhav", 67, 98, "Guddi", "54", "Dipanjali"]

########################################################################
# to get the last element of the list
# The reason of -1 is that according to len() function the list returns 7
# But list work on indexing number, and index starts from 0
# that's why -1 will give us the last element.
########################################################################
last_element = sample_list[len(sample_list) - 1]

# print the last element of the list
print(last_element)
