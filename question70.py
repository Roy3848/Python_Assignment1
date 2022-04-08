# Write a program to identify if number is palindrome or not
# As we are checking number. So 10 is the best to find the solution.

number = int(input("Enter a number: "))
temp = number  # set the number variable in another variable temp
# we expect that the value that we store will be reverse in the reverse variable.
reverse = 0

while number > 0:  # condition while number is greater than 0, the iteration happens
    digit = number % 10  # the remainder get store in the digit variable
    reverse = reverse * 10 + digit  # then the calculated result will be stored in the reverse
    number = number // 10  # and then update the number variable again

# then finally to check whether the number is palindrome or not
if temp == reverse:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")

print(reverse)
