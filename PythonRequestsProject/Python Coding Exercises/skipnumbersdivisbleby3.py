# Example 9: Skip numbers divisible by 3

for i in range(1, 111):  # numbers 1 to 10
    if i % 3 == 0:
        continue  # skip multiples of 3
    print(i)
else:
    print("Finished printing numbers 1–110, skipping multiples of 3.")
