# Anders Mortensen
# Dato: 15-04-2020

# Opgave 6

tal = int(input("Skriv et tal"))  #Beder dig om at skrive et tal og gemmer det

def vaniljebudding(tal):          #Definerer funktionen vaniljebudding for variablen tal
    if (tal % 3) == 0:            #Tjekker om det givne tal går op i tre
        if (tal % 5) == 0:        #Tjekker om det givne tal går op i fem
            return "vaniljebudding" #Hvis ja, så skrives der vaniljebudding
        else:
            return "vanilje"        #Hvis det er sandt at det går op i tre, men ikke fem, udskrives kun vanilje
    elif (tal % 5) == 0 and (tal % 3) > 0:   #Hvis det går op i fem, men ikke tre, så skrives der budding
            return "budding"
    else:                           #Hvis hverken tre eller fem går op i tallet, skrives der prøv igen
        return "Prøv igen"
    
print(vaniljebudding(tal))          #Udskriver