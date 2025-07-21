Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("   1) Dawn")
print("   2) Dusk")

Q1 = int(input("Response: "))

if Q1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
  print("Gryffindor:", Gryffindor)
  print("Ravenclaw:", Ravenclaw)
  print(" ")
elif Q1 == 2:
  Hufflepuff += 1
  Slytherin += 1
  print("Hufflepuff:", Hufflepuff)
  print("Slytherin:", Slytherin)
  print(" ")
else:
  print("Wrong input.")
  print(" ")

print("Q2) When I’m dead, I want people to remember me as:")
print("   1) The Good")
print("   2) The Great")
print("   3) The Wise")
print("   4) The Bold")

Q2 = int(input("Response: "))

if Q2 == 1:
  Hufflepuff += 2
  print("Hufflepuff:", Hufflepuff)
  print(" ")
elif Q2 == 2:
  Slytherin += 2
  print("Slytherin:", Slytherin)
  print(" ")
elif Q2 == 3:
  Ravenclaw += 2
  print("Ravenclaw:", Ravenclaw)
  print(" ")
elif Q2 == 4:
  Gryffindor += 2
  print("Gryffindor:", Gryffindor)
  print(" ")
else:
  print("Wrong input.")
  print(" ")

print("Q3) Which kind of instrument most pleases your ear?")
print("   1) The violin")
print("   2) The trumpet")
print("   3) The piano")
print("   4) The drum")

Q3 = int(input("Response: "))

if Q3 == 1:
  Slytherin += 4
  print("Slytherin:", Slytherin)
  print(" ")
elif Q3 == 2:
  Hufflepuff += 4
  print("Hufflepuff:", Hufflepuff)
  print(" ")
elif Q3 == 3:
  Ravenclaw += 4
  print("Ravenclaw:", Ravenclaw)
  print(" ")
elif Q3 == 4:
  Gryffindor += 4
  print("Gryffindor:", Gryffindor)
  print(" ")
else:
  print("Wrong input.")
  print(" ")

print("Gryffindor:", Gryffindor)
print("Ravenclaw:", Ravenclaw)
print("Hufflepuff:", Hufflepuff)
print("Slytherin:", Slytherin)
print(" ")

Houses = {
  "Gryffindor": Gryffindor,
  "Ravenclaw": Ravenclaw,
  "Hufflepuff": Hufflepuff,
  "Slytherin": Slytherin
  }

Sorting_Hat = max(Houses, key=Houses.get)
print(f"{Sorting_Hat} is the choice!")