# write a program to get all the even numbers from 0 to n (both included)
# Method 1
even_numbers = []  # an empty list to store the final list result
n = int(input("Enter a limit: "))  # ask the user to input the limit
for i in range(0, n+1):  # iteration over the range, n is included (so, n+1)
    if i % 2 == 0:
        even_numbers.append(str(i))  # in every iteration and condition holds true, even_numbers list gets append

print(even_numbers, end="")

# Method 2
print("\nUsing List Comprehension")
n1 = int(input("Enter a limit: "))
even_numbers_list = [str(i) for i in range(0, n+1) if i % 2 == 0]  # list comprehension with the same logic as above
print(even_numbers_list, end="")
