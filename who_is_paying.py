import random

# Split string method

#test_seed = int(input("create a seed number: "))
#random.seed(test_seed)


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#get the total number of items in list
num_items = len(names)
# generate random numbers between 0 and last name
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

# person_who_will_pay = random.choice(names)

print(f"the person that will pay the bill is {person_who_will_pay}")

