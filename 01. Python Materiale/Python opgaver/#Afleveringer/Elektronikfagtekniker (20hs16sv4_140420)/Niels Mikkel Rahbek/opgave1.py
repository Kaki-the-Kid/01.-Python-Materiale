# Mikkel Rahbek
# 15-04-2020
# Opgave 1

age = input("Hvornår er du født? ") # Laver age til input man skal taste
name = input("Hvad er dit navn? ") # Laver name til input man skal taste
x = 2020 # Sætter x til en værdi
x -= int(age) # Værdien x bliver fra trukket age, som er vigtig at lave til en int så den ved det er tal

print("Hej " + name) # Printer Hej efterfulgt navnet fra input
print("Du er, eller vil blive, " + str(x) + " år gammel i år") # Printer teksten og værdien af x. x er nu en string som hentes ind


