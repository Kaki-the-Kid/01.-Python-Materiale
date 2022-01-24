# Anders Chr. Rungborg
# 15-04-2020
# OPG Python

age = int(input("Indtast alder "))                                  # har er de input varjabler for aller 
price = int(input("indtast pris "))                                 # og pris 



if age < 12 :                                                   # vis allern er mindre enn 12 skal den sige "Din er grastis"
    #print("Din pris er " + str(float(price) * 0.0))
    print("Din er grastis")
    

if age < 24 and age >= 12:                            # og vis allern er 12 og op til 64 skal den * prisen med 0.3%
    print("Din pris er " + str(float(price) * 0.3) + "kr.")
    

if age > 65:
    print("Din pris er " + str(float(price) * 0.75) + "kr.")
    

if age > 24 and age <= 65 :
    print("Din pris er" + str(float(price)))




