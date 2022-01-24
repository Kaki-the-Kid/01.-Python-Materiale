# Anders Mortensen
# Dato: 15-04-2020

# Opgave 7

pris = int(input("Hvad er prisen?"))    #Beder dig om at indtaste en pris og gemmer den
alder = int(input("Hvad er din alder")) #Beder dig om at indtaste en alder og gemmer den

if alder < 12:                  #Hvis du er under 12, så skriver den: "Du er gratis"
    print("Du er gratis")
    
if alder > 11 and alder < 25:   #Hvis du er imellem 12 og 24, så tager den kun 70% af beløbet
    
    print("Prisen er " + str(float(pris) * 0.70) + "kr")
    
if alder > 23 and alder < 66:   #Hvis du er imellem 24 og 65, så betaler du fuld pris
    print("Prisen er " + str(float(pris) * 1) + "kr")
    
if alder > 65:                  #Hvis du er over 65, betaler 75% af beløbet
    print("Prisen er " + str(float(pris) * 0.75) + "kr")