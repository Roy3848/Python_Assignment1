# Define a function that can accept two strings as input and
# print the string with maximum length in the console. If two strings have the same length,
# then the function should print all strings line by line.

def two_strings(string1, string2):
    if len(string1) > len(string2):
        print(string1)
    elif len(string2) > len(string1):
        print(string2)
    elif len(string1) == len(string2):
        print(string1, string2, sep="\n")
    else:
        print("Invalid String!!!")


two_strings(input("Enter a string: "), input("Enter another string: "))
