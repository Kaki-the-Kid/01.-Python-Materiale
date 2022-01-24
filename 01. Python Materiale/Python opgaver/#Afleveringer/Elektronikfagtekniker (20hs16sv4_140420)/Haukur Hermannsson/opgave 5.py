# Haukur
# 15.04.2020
# Opgave 5

# Grænse udregning om hvilke film man må se.

age = int(input("Hvad er din alder? "))    # Kig efter integer type input (alder)


if age > 17:                               # Kig efter at tallet er over 17
    print("Du kan se film der er Rated-R") # Hvis alderen er over 17 så returnér med "Rated-R"

if age < 17 and age > 13:                  # Kig efter at tallet er under 17 og over 13
    print("Du kan se film der er PG-13")   # Hvis den er under 17 og over 13 så returnér med "PG-13"

if age < 13:                               # Kig efter at tallet er mindre end 13
    print("du kan se film der er PG")      # Hvis den er mindre end 13 så returnér med "PG"
    
    
    
