#Password Generator Project
import random
import data

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many characters?\n"))


password = []
for _ in range(1, random.randint(18,25)):
  password.append(random.choice(data.letters))
random.shuffle(password)
password =''.join(password)
print(password)
pass_lenght=(len(password))

print(f"Your password has: {pass_lenght} characters\n")

# r_characters = random.randint(18,25)
# print(r_characters)