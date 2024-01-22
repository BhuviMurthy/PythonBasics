# Write your code here 👇

target = 100
for number in range(1,target+1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0: 
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
 

 #output 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz.....
