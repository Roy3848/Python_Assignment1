# Write a program which accepts comma separated string
# and return the output alphabetically
# method 1 (using list comprehension)
items1 = input("Insert comma separated sequence of word: ")
new_list1 = [word1 for word1 in items1.split(", ")]
print(", ".join(sorted(new_list1)))
