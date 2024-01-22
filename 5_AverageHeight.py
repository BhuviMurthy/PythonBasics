# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_heights = 0
# 🚨 Don't change the code above 👆
for height in student_heights:
  total_heights += height
print(f"total height = {total_heights}")
number_of_students = len(student_heights)
print(f"number of students = {number_of_students}")

average_height = total_heights / number_of_students
average_height = round(average_height)
# Write your code below this row 👇
print(f"average height = {average_height}")
