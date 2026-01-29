balance = 5001  # initial balance
withdrawals = [100, 50, 200, 300]  # list of amounts to withdraw

i = 0  # index for withdrawals
while i < len(withdrawals):
    if withdrawals[i] <= balance:
        balance -= withdrawals[i]
        print(f"Withdrew {withdrawals[i]}, remaining balance: {balance}")
    else:
        print(f"Cannot withdraw {withdrawals[i]} - insufficient funds.")
    i += 1
else:
    print(f"All transactions processed. Final balance: {balance}")
