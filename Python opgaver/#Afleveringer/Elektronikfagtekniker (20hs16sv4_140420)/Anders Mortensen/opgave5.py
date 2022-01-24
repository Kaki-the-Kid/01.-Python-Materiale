# Anders Mortensen
# Dato: 15-04-2020

# Opgave 5

alder = input("Hvor gammel er du?") #Spørger hvor gammel du er og venter på et input.

if int(alder) >= 18:                #Fortæller dig, at du må se R-rated film, hvis inputtet er over 18.
    print("R-rated godkendt")
if int(alder) >= 13:                #Fortæller dig, at du må se PG-13 film, hvis du er 13 eller over. 
    print("PG-13 godkendt")
    
print ("PG godkendt")               #Fortæller dig, at du må se PG film, da det er for alle aldre.
    
    
