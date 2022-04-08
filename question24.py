# Divides Evenly
# Returns True if a can be evenly divided by b.

def evenly_divisible(a, b):
    if a % b == 0:  # conditional statement to check whether 'a' is evenly divided by b.
        return True  # return true if yes
    else:
        return False  # else return false


# calling out the function
print(evenly_divisible(int(input("Enter a dividend: ")), int(input("Enter a divisor: "))))

