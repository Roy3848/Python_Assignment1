# write a program to perform all basic mathematical operations

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
op = input("Enter an operator: ")


# with the conditional statements checking of all the operators
# and to perform the same operation with the numbers taken as an input from the user
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(abs((num1 - num2)))
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(abs(num1 / num2))
elif op == "%":
    print(abs(num1 % num2))
else:
    print("Invalid Operator!!!")

print("This is the result.")
