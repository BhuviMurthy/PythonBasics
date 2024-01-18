import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

if user_input == "0":
  print(rock)
elif user_input == "1":
  print(paper)
else:
  print(scissors)

random_number = random.randint(0,2)

print("Computer chose:")
if random_number == "0":
  print(rock)
elif random_number == "1":
  print(paper)
else:
  print(scissors)

if user_input == "0" and random_number == "0":
  print("Draw")
elif user_input == "0" and random_number == "1":
  print("Computer won")
elif user_input == "0" and random_number == "2":
  print("You won")
elif user_input == "1" and random_number == "0":
  print("You Won")
elif user_input == "1" and random_number == "1":
  print("Draw")
elif user_input == "1" and random_number == "2":
  print("Computer won")
elif user_input == "2" and random_number == "0":
  print("Computer won")
elif user_input == "2" and random_number == "1":
  print("You won")
else:
  print("Draw")
