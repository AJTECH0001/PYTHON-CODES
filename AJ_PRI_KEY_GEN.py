#Password Generator Project
import random
letters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']



print("Welcome to AJ PRIVATE_KEY Generator!")

nr_letters= 64

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
for char in range (1, nr_letters + 1):
    password_list.append(random.choice(letters))


print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")