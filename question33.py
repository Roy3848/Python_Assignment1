# write a program to check the validity of password input by the users

# importing regular expression module
import re

# asking the user to input a password
password = input("Enter password: ")
# flag acts as a signal to the program
# to determine whether the whole program will run
# or only a specific part of the program should run
flag = 0
while True:
    if len(password) < 8:
        flag = -1
        break
    # re module has search function checks the input by the user
    # whether the input satisfies the given pattern.
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")
