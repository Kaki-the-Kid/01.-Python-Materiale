# Mikkel
# 15-04-2020
# Opgave 6

tal = int(input("indsæt tallet fra 1 til og med 25 ")) # laver strengen tal

def replaceNumbers(tal): # Definerer funktionen replaceNumbers med input-parameteret n.
    if (tal % 3) == 0: # Hvis tal % 3 = 0 (tal går op i 3).
        if (tal % 5) == 0: # og hvis tal % 5 = 0 (går op i 5).
            return "vaniljebudding" # Returnér strengen "vaniljebudding".
        else: # Ellers.
            return "vanilje" # tal går op i 3 men ikke i 5. returnér strengen "vanilje".
    elif (tal % 5) == 0 and (tal % 3) > 0: # Eller hvis tal går op i 5 og tal ikke går op i 3.
        return "budding" # Returnér strengen "budding".

    else: # Ellers.
        return "Prøv igen! Dit tal går ikke op i 3, 5 eller begge dele" # Returnér strengen.


print(replaceNumbers(tal)) # Udskriver resultatet af replaceNumber-funktionen. Hvor inputtet er x fra for-loopet.


