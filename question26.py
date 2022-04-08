# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# You can take any range like 2000-4700 or 3800-4900 etc.
# Check if both range number also included in output

# function which takes to arguments one is the starting point of the range
# the another is the ending point of the range
def myfunction(start, end):
    for i in range(start, end+1):  # then to iterate over the range
        if i % 7 == 0 and i % 5 != 0:  # to check with the conditional statement
            print(i, end=" ")


myfunction(100, 500)
