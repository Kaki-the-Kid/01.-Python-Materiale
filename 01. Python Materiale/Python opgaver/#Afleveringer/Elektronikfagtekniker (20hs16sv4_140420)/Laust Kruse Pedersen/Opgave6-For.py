#Navn: Laust Kruse Pedersen
#Dato: 15/01/2020
#Opgave: 6

#For lykke der tæller fra 1 til 25.
for x in range(1,26):
    #If tallet kan deles med både 3 og 5.
    if x % 3 == 0 and x % 5 == 0:
        print("vaniljebudding")
    #If tallet kan delses med 5.
    elif x % 5 == 0:
        print("budding")
    #If tallet kan delses med 3.
    elif x % 3 == 0:
        print("vanilje")
    #If tallet ikke kan delse med 3 eller 5.
    else:
        print(x)
        