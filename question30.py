# Write a program that accepts a sentence
# and calculate the number of letters and digits
# and also calculates the upper and lower case letters

# Write a program that accepts a sentence
# and calculate the number of letters and digits
# and also calculates the upper and lower case letters

string = input("Enter a string: ")
digit = 0  # a variable to store the count of digits in the sentence
letters = 0  # a variable to store the count of letters in the sentence
upper_case = 0  # a variable to store the count of upper_case in the sentence
lower_case = 0  # a variable to store the count of lower_case in the sentence

for i in string:
    if i.isdigit():
        digit = digit + 1  # everytime digit comes, the digit variable increment by 1
    elif i.isalpha():
        letters = letters + 1  # everytime letters comes, the letters variable increment by 1
        # upper_case and lower_case are also letters, so conditional indented inside the letters condition
        if i.isupper():
            upper_case = upper_case + 1  # everytime upper_case letters comes, the upper_case variable increment by 1
        elif i.islower():
            lower_case = lower_case + 1  # everytime lower_case letters comes, the lower_case variable increment by 1
    else:
        pass

print("Total digits are: {}.".format(digit))
print("Total letters are: {}.".format(letters))
print("Total upper case letters are {}.".format(upper_case))
print("Total lower case letters are {}.".format(lower_case))

