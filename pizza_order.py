print ("Welcome to AJ pizza deliveries!")
size = input("What size pizza do you want? S, M OR L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input ("do you want extra cheese? Y or N\n")
bill = 0

if size == "S":
    bill += 15
elif size == "L":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
      bill += 2
    else:
      bill +=3

if extra_cheese == "Y":
   bill +=1

print(f"your final bill is ${bill}")
   


