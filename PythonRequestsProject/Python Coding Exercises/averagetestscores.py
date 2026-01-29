scores = [80.0, 85.0, 90.0, 75.0]  # list of test scores (floats)
total = 0.0  # initialize total as float

for score in scores:
    total += score
else:
    average = total / len(scores)  # compute average after loop
    print(f"Average score: {average}")
