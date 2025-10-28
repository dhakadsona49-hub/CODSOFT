import random

print("----- Password Generator -----")

# Ask the user to enter the length of the password
password_length = int(input("Enter the desired password length: "))

# Characters to be used in password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+[]{}<>?/|"

all_characters = letters + numbers + symbols

password = ""

# Generate password
for i in range(password_length):
    password += random.choice(all_characters)

# Show generated password
print("\n✅ Your Generated Password is:", password)
