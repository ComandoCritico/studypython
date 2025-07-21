import random

grade = random.randint(0, 100)

if grade >= 55:
  print("You passed.", grade)
else:
  print("You failed.", grade)