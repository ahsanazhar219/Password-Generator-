import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

def generate_password(length):
  """Generates a secure password with letters, numbers, and symbols."""

  password_list = []
  password_list += random.sample(letters, length // 3)
  password_list += random.sample(numbers, length // 3)
  password_list += random.sample(symbols, length // 3)
  random.shuffle(password_list)
  password = "".join(password_list)
  return password

# Get user input for desired password length
desired_length = int(input("Enter the desired password length: "))

# Ensure length is reasonable for security
while desired_length < 8:
  print("Password length should be at least 8 characters.")
  desired_length = int(input("Enter the desired password length: "))

# Generate and print the password
password = generate_password(desired_length)
print("Your secure password is:", password)
