ph = int(input("Enter a ph value (0-14): "))

if ph > 7:
  print("Basic", ph)
elif ph < 7:
  print("Acidic", ph)
else:
  print("Neutral", ph)