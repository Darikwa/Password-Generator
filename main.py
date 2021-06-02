#Password Generator Project
import random
import data

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many characters?\n"))
print('Your password is: \n')

password = []
for _ in range(1, nr_letters + 1):
  password.append(random.choice(data.letters))
random.shuffle(password)
password =''.join(password)
print(password)