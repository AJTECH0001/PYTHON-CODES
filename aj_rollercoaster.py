print("Welcome to AJ rollercoster funpark")

Height = int(input("what is your height?"))
bill = 0

if Height > 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("child tiickets are $5")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7")
    elif age >=45 and age <=55 :
        print("everything is going to be okay. have a free ride on us")
    else:
        print("adult tickets are $12")
   
    wants_photo = input("do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
        print(f"your total is {bill}")
else:
    print("sorry you have to grow taller before you can ride")