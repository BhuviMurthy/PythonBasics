target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

even = 0
# Write your code here 👇
for number in range(2,target+1,2):
  even += number

print(even)

#input is 52 then target is set as 52 then adding will start from 2 till 52 (52+1) range will always take (n-1) output will be 702
