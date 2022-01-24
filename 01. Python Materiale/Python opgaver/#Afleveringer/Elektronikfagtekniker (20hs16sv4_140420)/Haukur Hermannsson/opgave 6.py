# Haukur
# 15.04.2020
# Opgave 6

# Spil med regler.

def replaceNumbers(n):                  # Definerer funktionen replaceNumbers med input-parameteret n.
    if (n % 3) == 0:                    # Hvis n går op i 3
        if (n % 5) == 0:                # Og hvis n går op i 5
            return "vaniljebudding"     # Så returnér den "vaniljebudding".
        else:                           
            return "vanilje"            # Hvis n går op i 3 men ikke i 5. returnér den "vanilje".
    elif (n % 5) == 0 and (n % 3) > 0:  # Eller hvis n går op i 5 og n ikke går op i 3.
        return "budding"                # Returnér "budding".

    else:                               
        return n                        # Ellers returnér n.

for x in range(0,25):                   # Kør indholdet af for-loopet 25 gange. x bliver talt op hver gang loopet køres.
    print(replaceNumbers(x))            # Udskriver resultatet af replaceNumber-funktionen. Hvor inputtet er x fra for-loopet.
