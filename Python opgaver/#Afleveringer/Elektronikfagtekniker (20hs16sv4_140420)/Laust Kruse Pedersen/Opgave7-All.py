#Navn: Laust Kruse Pedersen
#Dato: 15/01/2020
#Opgave: 7
#Inputs til billet pris og alder.
pris = float(input("Hvor meget skal du betale? "))
age = int(input("Hvor gammel er du? "))

#If alderen er under 12 er der 100% rabat.
if age < 12:
    rate=0
#If alderen er under 24 er der 30% rabat.   
elif age < 24:
    rate=0.70
#If alderen er mellem 24 og 65 er der ingen rabat.     
elif age < 65:
    rate=1
#If alderen er mere end 65 er der 25% rabat.     
else:
    rate=0.75

#Printer prisen på billeten efter rabat i kr.
print("Du skal betale: " + str(pris*rate) + "kr")