#Navn: Laust Kruse Pedersen
#Dato: 15/01/2020
#Opgave: 2

#Variabel med en sætning.
txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
tar = "ipsum"

#Print den ønsked del.
print("Slice: " + txt[6:11])

#Finder starten på den ønsked del.
x = txt.find(tar)
#Finder længten på den ønsked del.
y = x+len(tar)
#Printer den ønsked del.
print("Finde: " + txt[x:y])
