#Password Generator Project
import random
import lettersNumsSymbols

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print('Your password is: \n')

password = []
for char1 in range(1, nr_letters + 1):
  password.append(random.choice(lettersNumsSymbols.letters)) #you can 
for char2 in range(1, nr_symbols + 1):
  password += random.choice(lettersNumsSymbols.symbols)
for char3 in range(1, nr_numbers + 1):
  password += random.choice(lettersNumsSymbols.numbers)
#print(password)
random.shuffle(password)
#print(password)
password =''.join(password)
print(password)