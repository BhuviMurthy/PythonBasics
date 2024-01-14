#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
bill = float(input("What was the total bill? $"))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
tip = int(input("ow much tip would you like to give? 10, 12, or 15?"))
percentage = 100.00
total_bill = tip / percentage * bill + bill

                                              
#Write your code below this line 👇
split = int(input("How many people to split the bill?"))

amount = round((total_bill / split),2)
amount = "{:.2f}".format(amount)

print(f"Each person should pay: {amount}")
