# Anders Chr. Rungborg
# 15-04-2020
# OPG Python

age = input("Indtast alder ")                                  # har er de input varjabler for aller 
price = input("indtast pris ")                                 # og pris 

a = "12"
b = "24"
c = "65"

if age < a :                                                   # vis allern er mindre enn 12 skal den sige "Din er grastis"
    #print("Din pris er " + str(float(price) * 0.0))
    print("Din er grastis")
    

if age < b and age > c or age == a:                            # og vis allern er 12 og op til 64 skal den * prisen med 0.3%
    print("Din pris er " + str(float(price) * 0.3))
    

if age > c:
    print("Din pris er " + str(float(price) * 0.75))
    

if age > b and age < c or age == b:
    print("Din pris er" + str(float(price)))




