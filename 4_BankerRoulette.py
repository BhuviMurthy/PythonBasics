names = names_string.split(", ")
# The code above converts the input into an array separating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
num_items = len(names)
random_names = random.randint(0, num_items -1)

person_pay = names[random_names]
print(f"{person_pay} is going to buy the meal today!")

#input => names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"] --> list of names
