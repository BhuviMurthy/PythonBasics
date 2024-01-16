#This is an example of Nested if else statement and multiple if statement
print("Welcome to the rollercoaster")
height = int(input("What is your height in cms"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("The ticket cost is $5")
        bill = 5
    elif age <= 18:
        print("The ticket cost is $7")
        bill = 7
    else: 
        print("The ticket cost is $12")
        bill = 12
    want_photo = input("Do you want a photo? Y or N")
    if want_photo == 'Y':
        bill += 3;
        print(f"Your total charge is ${bill}")
    else:
        print(f"Your total charge is ${bill}")
        
else:
    print("Sorry, You cannot ride the rollercoaster")
