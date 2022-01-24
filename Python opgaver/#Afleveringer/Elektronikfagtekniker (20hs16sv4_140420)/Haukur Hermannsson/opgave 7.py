# Haukur
# 15.04.2020
# Opgave 7

# Udregning af billetpriser med hensyn til alder.

price = int(input("Hvad koster billeten? "))                                    # Kigger efter integer type input (pris)
age = int(input("Og hvor gammel er du? "))                                       # Kigger efter integer type input (alder)                                              #


if age < 12:                                                                     # Hvis alderen er under 12
    print("Tillykke! Din billet er gratis!")                                     # Så skriver den at billetten er gratis
     
if age < 24 and age >= 12:                                                       # Hvis alderen er 12 eller over og under 24
    print("Din billet kommer til at koste " + str(float(price) * 0.3) + " kr.")  # Så skriver den at prisen med en 70% rabat
    
if age >= 24 and age < 65:                                                       # Hvis alderen er 24 eller over og under 65
    print("Din billet kommer til at koste " + str(float(price)) + " kr.")        # Så skriver den uændret pris.
    
if age >= 65:                                                                    # Hvis alderen er over 65
    print("Din billet kommer til at koste " + str(float(price) * 0.25) + " kr.") # Så skriver den at prisen med en 75% rabat