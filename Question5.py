# Convert string into integer
# int() function is used to do the same.
# can be checked with type() function whether changed or not
# METHOD 1

# variable to enter age
age = input("what is your age: ")
print(age)

# to check the type of the variable age
print(type(age))


# converted the age variable from string to integer.
age = int(input("Enter your age: "))
print(age)

# again check the type of the variable age.
# this time it will be showing the type integer
print(type(age))

# METHOD 2

# defining a function to change type of the variable
def age_string(para):
	return int(para)  # return the integer datatype of the variable from the string datatype
	

print(age_string(input("Enter a number string: ")))  # will return the age in integer

# to check whether it really changed or not
print(type(age_string(age)))

