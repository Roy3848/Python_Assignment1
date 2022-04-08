# Define class/ function which has at least two methods
# getString: To get a string from console input
# printString: to print the string in upper case


# class called Two_methods
class TwoMethods:
    def __init__(self):
        self.str1 = " "  # an empty string  (setting the attributes)

    def get_string(self):  # the methods(function inside the class) get_string to get the input from the user
        self.str1 = input("Enter a string: ")

    def print_string(self):  # method (function inside the class) print_string to print the output
        # after converting the string into uppercase
        print(self.str1.upper())


str1 = TwoMethods()
str1.get_string()
str1.print_string()
