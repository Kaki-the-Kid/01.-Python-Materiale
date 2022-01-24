#Navn Thomas Suder
#Dato 15/04/2020
#Opgave 6

#For lykke der tæller fra 1 til 25.
for x in range (1,25):
    #hvis tallet kan deles med både 3 og 5.
    if x % 3 == 0 and x % 5 == 0:
        print("vaniljebudding")
        # hvis tallet kan deles med 3.
    elif x % 3 == 0:
        print("vanilje")
        #hvis tallet kan deles med 5.
    elif x % 5 == 0:
        print("budding")
        #Alle andre tal falder under denne kategori.
    else:
        print(x)