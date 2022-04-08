# Write  program to accept a string from the user
# and return the string in the reverse order

# Method 1 (using slicing)
string = input("Enter a string: ")


def reverse_string(word):
    return word[::-1]


print(reverse_string(string))


# method 2 (using reverse method)
string1 = input("Enter  a string: ")


def reverse_string1(word):
    return reverse_string(word)


print(reverse_string1(string1))
