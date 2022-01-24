#Navn: Laust Kruse Pedersen
#Dato: 15/01/2020
#Opgave: 5

#Input til din alder.
age = int(input("Hvor gammel er du? "))

#If lykke der spørg om man er over 18.
if 18 <= age:
    print("Du må se R rated film")    
#Else If der spørg om man er mellem 13 og 18.    
elif 13 <= age < 18:
    print("Du må se PG-13 rated film")    
#Else der fanger aller andre muligheder.    
else:
    print("Hvis du er usikker eller under 13 må du se PG rated film")
    
