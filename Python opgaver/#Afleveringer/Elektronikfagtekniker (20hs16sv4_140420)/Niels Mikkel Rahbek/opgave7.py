# Mikkel
# 15-04-2020
# Opgave 7

alder = int(input("indtast din alder ")) # streng med alder i tal
pris = int(input("intast prisen på billetten ")) # streng med pris i tal

if alder < 12: # hvis alder er mindre en 12
    print("Din billet er gratis") # udskriv strengen
    
if alder > 11 and alder < 24: # hvis alder er større en 11 og mindre en 24
    print("Din billet koster " + str(float(pris) * 0.3) + "kr") # udskriver strengen, hvor prisen bliver ganget med 0.3(float så den kan tage decimaler)
    
if alder > 23 and alder < 65: # hvis alder er større end 23 og mindre end 65
    print("Din billet koster " + str(float(pris)) + "kr") # udskriver strengen, med prisen(float så den kan tage decimaler)
    
if alder > 64: # hvis alder er større end 64
    print("Din billet koster " + str(float(pris) * 0.25) + "kr") # udskriver strengen, hvor prisen bliver ganget med 0.25(float så den kan tage decimaler)
    
    