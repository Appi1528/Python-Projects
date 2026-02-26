import random
import string

print("Password Generator")

# User input
length = int(input("Enter the desired password length: "))

print("Choose password complexity:")
print("1. Letters only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Symbols")

choice = input("Enter choice (1/2/3): ")

# Character sets
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

if choice == '1':
    characters = letters
elif choice == '2':
    characters = letters + numbers
elif choice == '3':
    characters = letters + numbers + symbols
else:
    print("Invalid choice! Defaulting to Letters only.")
    characters = letters

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display password
print("Generated Password:", password)
