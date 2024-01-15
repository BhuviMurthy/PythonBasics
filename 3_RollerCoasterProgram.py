#This is an example of Nested if else statement 
print("Welcome to the rollercoaster")
height = int(input("What is your height in cms"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("The ticket cost is $5")
    elif age <= 18:
        print("The ticket cost is $7")
    else: 
        print("The ticket cost is $7")
else:
    print("You cannot ride the rollercoaster")
