"""
Python Beginner Keywords Demo
- Demonstrates key Python keywords with examples
"""

# --- Flow Control ---
print("=== Flow Control ===")
age = 15
if age >= 18:
    print("You can vote")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# pass example
if age > 0:
    pass  # does nothing

print("-" * 20)

# --- Loops ---
print("=== Loops ===")
# for loop
for i in range(3):
    print(f"For loop iteration {i}")

# while loop
count = 0
while count < 3:
    print(f"While loop iteration {count}")
    count += 1

# break and continue
for i in range(5):
    if i == 3:
        break  # stop loop
    if i == 1:
        continue  # skip this iteration
    print(f"i = {i}")

print("-" * 20)

# --- Functions ---
print("=== Functions ===")


def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))

# lambda function
square = lambda x: x * x
print("Square of 4:", square(4))

print("-" * 20)

# --- Boolean / Logic ---
print("=== Boolean / Logic ===")
x = 5
y = 10
flag = True

if x < y and flag:
    print("x < y and flag is True")
if x > y or flag:
    print("x > y or flag is True")
if not x > y:
    print("not x > y is True")

print("True value:", True)
print("False value:", False)
print("None value:", None)

print("-" * 20)

# --- Membership / Identity ---
print("=== Membership / Identity ===")
nums = [1, 2, 3]
if 2 in nums:
    print("2 is in the list")

a = [1, 2]
b = a
if a is b:
    print("a is b (same object)")

print("-" * 20)

# --- Import Modules ---
print("=== Import Modules ===")
import math
from math import sqrt

print("sqrt(16):", sqrt(16))
import math as m

print("cos(0):", m.cos(0))

print("-" * 20)

# --- Scope / Resource Management ---
print("=== Scope / Resource Management ===")
# del example
my_list = [10, 20, 30]
del my_list[1]
print("After deletion:", my_list)

# with example (context manager)
with open("demo.txt", "w") as f:
    f.write("Hello from Python!")

print("Check demo.txt file created")
