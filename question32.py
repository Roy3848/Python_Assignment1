# Write a computer program that computes the net amount of a bank account
# Interactive bank account Calculator

total_transaction = int(input("Enter the total number of transaction: "))  # user input for total transactions
total_deposit = int(input("Total number of deposits: "))  # user input total deposits in that transactions
total_withdraw = int(input("Total number of withdrawals: "))  # user input total withdraw in that total transaction
transaction_count = 0  # variable set to 0 for reference, because of the comparison with total_transaction
deposit = 0  # deposit variable initially set to 0, to get added with the amount of deposit over the iteration
withdraw = 0  # withdraw variable initially set to 0, to get added with the amount of withdraw over the iteration
transaction_start = input("Transaction start: ")

# till the transaction count is less than the total transaction
# the loop continues iteration
while transaction_count < total_transaction:
    # based on the answer by the user (in Y or N)
    # the transaction either starts or not
    if transaction_start.upper() in "Y":
        deposit_or_withdraw = input("Deposit or withdraw: ")
        # Based on the user input (whether to deposit or withdraw)
        if deposit_or_withdraw.upper() in "D":
            deposit_amount = int(input("Enter deposit amount: "))
            deposit = deposit + deposit_amount  # if deposited, then deposit variable increases by the amount mentioned
            transaction_count = transaction_count + 1  # over every iteration the transaction count increase by 1
        elif deposit_or_withdraw.upper() in "W":
            withdraw_amount = int(input("Enter withdraw amount: "))
            withdraw = withdraw + withdraw_amount  # if withdrew, then withdraw variable increases by the amount mention
            transaction_count = transaction_count + 1  # over every iteration the transaction count increases by 1
        else:
            print("Invalid transaction!!!")
    elif transaction_start.upper() in "N":
        print("Everything is Cleared.")
    else:
        pass


total_amount = deposit - withdraw  # at last to compute the actual amount of the user bank account
print("The total amount in your bank is {}.".format(total_amount))
