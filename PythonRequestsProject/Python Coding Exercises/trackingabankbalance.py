balance = 5290.0  # initial balance
withdrawals = [100.0, 50.0, 200.0, 180.0]  # list of amounts to withdraw
threshold = 100.0  # low balance threshold

i = 0  # index for withdrawals
while i < len(withdrawals) and balance > threshold:
    if withdrawals[i] <= balance:
        balance -= withdrawals[i]
        print(f"Withdrew {withdrawals[i]}, remaining balance: {balance}")
    else:
        print(f"Cannot withdraw {withdrawals[i]} - insufficient funds.")
    i += 1
else:
    if balance <= threshold:
        print("Low balance warning.")
    else:
        print("All transactions processed. Final balance:", balance)
