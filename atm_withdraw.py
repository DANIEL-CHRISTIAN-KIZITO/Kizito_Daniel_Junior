# ATM Withdrawal Program

# Initial account balance
account_balance = 1000.00  # You can set this to any amount

# Display balance
print("Welcome to the ATM!")
print(f"Your current account balance is: UGX{account_balance:.2f}")

# Prompt user for withdrawal amount
withdraw_amount = float(input("Enter amount to withdraw: UGX"))

# Check if withdrawal is possible
if withdraw_amount <= 0:
    print("Withdrawal amount must be greater than zero.")
elif withdraw_amount > account_balance:
    print("Insufficient balance. Transaction denied.")
else:
    account_balance -= withdraw_amount
    print(f"Transaction successful! You withdrew UGX{withdraw_amount:.2f}")
    print(f"Remaining balance: UGX{account_balance:.2f}")
