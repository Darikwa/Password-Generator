#Password Generator Project
import random
import data

print("Random Password Generator!\n")

password = []
for _ in range(1, random.randint(18,25)):
  password.append(random.choice(data.letters))
random.shuffle(password)
password =''.join(password)
print(f'Your Password is:\n{password}\n')

print(f"Your password has: {len(password)} characters\n\nThanks You 😊")
