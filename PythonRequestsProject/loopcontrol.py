"""
Training loop control
- Demonstrates for loops
- Demonstrates while loops
- Demonstrates dictionaries
- Prints "Go To Hell" 5 times
"""

# For loop control
num = int(input("Enter a number: "))
for i in range(1, 6):
    print(num, "*", i, "=", num * i)

print("-" * 20)  # Separator

# While loop control
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(num, "*", i, "=", num * i)
    i += 1

print("-" * 20)  # Separator

# Print "Go To Hell" 5 times
i = 0
while True:
    print("Go To Hell")
    i += 1
    if i == 5:
        break

# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create a dictionary to store word lengths
word_lengths = {}

# Fill dictionary
for word in words:
    word_lengths[word] = len(word)

# Print dictionary items
print("Word lengths:")
for word, length in word_lengths.items():
    print(f"{word}: {length}")

print("-" * 20)

# While loop: print each word in uppercase
i = 0
while i < len(words):
    print(words[i].upper())
    i += 1

print("-" * 20)

# Print "Go To Hell" 5 times again
i = 0
while True:
    print("Go To Hell")
    i += 1
    if i == 5:
        break
