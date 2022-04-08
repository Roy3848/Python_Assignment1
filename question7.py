# POWER CALCULATOR
# METHOD 1 (single iteration)
base_number = int(input("Enter a base_number: "))  # Enter one number in this variable
power_number = int(input("Enter a power number: "))  # input for the user using this variable
result = base_number ** power_number  # formula to power the number (can also use math module)
print(result)  # print out the result.

# METHOD 2 (to make the loop infinite using "while" loop)
while True:  # to make an infinite loop
    base_number = int(input("Enter a base_number: "))
    power_number = int(input("Enter a power_number: "))
    result = base_number ** power_number
    print(result)
    break  # break statement to end the infinite loop once we find our result.
