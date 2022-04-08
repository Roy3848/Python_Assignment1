# Check if an integer is divisible by 5
num = int(input("Enter any number: "))  # variable to ask the user to input the value

# defining function to find the divisible by 5
def divisible_five(n):
    if n % 5 == 0:  # condition of whether divisible by 5 or not
        return True  # return true if divisible by 5
    else:
        return False  # else return False


# calling out the function to run the function
print(divisible_five(num))
