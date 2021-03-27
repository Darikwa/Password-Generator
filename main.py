#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print('Your password is: \n')
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# randomLetters = (random.choices(letters, k=nr_letters))
# randomNumbers = (random.choices(numbers, k=nr_numbers))
# randomSymbols = (random.choices(symbols, k=nr_symbols))
# password = ''.join(randomNumbers + randomLetters + randomSymbols).split() #''.join turns arrays into text
# random.shuffle(password)
# #randPass = ''.join(random.choices(password, k=len(password)))
# print(password)
# #print(randPass)

# password = ''
# for char1 in range(1, nr_letters + 1):
#   password += random.choice(letters)
# for char2 in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
# for char3 in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for char1 in range(1, nr_letters + 1):
  password.append(random.choice(letters)) #you can 
for char2 in range(1, nr_symbols + 1):
  password += random.choice(symbols)
for char3 in range(1, nr_numbers + 1):
  password += random.choice(numbers)
#print(password)
random.shuffle(password)
#print(password)
password =''.join(password)
print(password)