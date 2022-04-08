# Check char is digit without using isdigit() , take input from console

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list1 = []
character = input("Enter the char\n")
# making the list1 of digit and no digit elements
for i in character:
    if i in numbers:
        list1.append("Digit")
    else:
        list1.append("No Digit")
a = "No Digit"  # setting the variable 'a' to no digit
# then to check whether the digit or not
if a in list1:
    print("This char is not a digit")
else:
    print("This char is a digit")
    b = int(character)
    print(type(b))





