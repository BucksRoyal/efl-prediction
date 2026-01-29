miles = float(input("Enter distance in miles: "))

# Conversion factor
km_factor = 1.609  # 1 mile = 1.609 kilometers

# Convert to kilometers
kilometers = miles * km_factor

# Print result rounded to 2 decimal places
print(f"Distance in km: {kilometers:.2f}")
