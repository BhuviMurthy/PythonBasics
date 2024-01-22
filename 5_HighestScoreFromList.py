# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
sample_score = 0
for score in student_scores:
  if score > sample_score:
    sample_score = score
  

# Write your code below this row 👇
print(f"The highest score in the class is: {sample_score}")
