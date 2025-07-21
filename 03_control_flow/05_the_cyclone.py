height = int(input("Height: "))
credits = int(input("Credits: "))

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif credits >= 10 and height < 137:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print ("You don't have enough credits.")
else:
  print("No, you can't.")