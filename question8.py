# Conversion from boolean to string
# METHOD 1

boolean = True  # variable to store boolean values
boolean_conversion = str(boolean)  # convert the boolean value into strin.
print(boolean_conversion)  # print the output
# to check whether it changed to string
print(boolean)

# to check whether the variable really changed from boolean to string
print(type(boolean_conversion))


# METHOD 2 (using function)

# defining a function for the conversion from boolean to string
def boolean_conversion(boolean_value):
    return str(boolean_value)  # return the string version of the variable


print(boolean_conversion(True))
# To check whether it really changed or not
print(type(boolean_conversion(True)))
