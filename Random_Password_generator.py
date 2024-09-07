import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

password = []

nr_letters = int(input("How many letters would you like in your password?\n"))

for i in range(nr_letters):
    z = random.choice(letters)
    password.append(z)

nr_symbols = int(input(f"How many symbols would you like?\n"))

for i in range(nr_symbols):
    x = random.choice(symbols)
    password.append(x)


nr_numbers = int(input(f"How many numbers would you like?\n"))

for i in range(nr_numbers):
    y = random.choice(numbers)
    password.append(y)

random.shuffle(password)


print("Here is your New Password")
print(''.join(password))
