# Mikkel
# 15-04-2020
# Opgave 5

age = input("Hvor gammel er du? ")


if int(age) < 13:
    print("Din rating er: PG")
    
if int(age) < 18 and int(age) > 12:
    print("Din rating er: PG-13")
    
if int(age) > 17:
    print("Din rating er: R")
    


