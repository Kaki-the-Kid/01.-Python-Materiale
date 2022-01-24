#/bin/python3.7																#Specificerer interpreter

def getPrice(alder):														#Definerer funktionen getPrice med input-parameteret alder.
	if alder < 12:															#Hvis alder er under 12.
		return 0.0															#Returnér 0.0 (0 %).
	elif alder < 24 and alder >= 12:										#Ellers hvis alder er under 24 OG alder er større end, eller lig med 12.
		return 0.7															#Returnér 0.7 (70 %).
	elif alder < 65 and alder >= 24:										#Ellers hvis alder er mindre end 65 OG alder er større end, eller lig med 24.
		return 1.0															#Returnér 1.0 (100 %).
	else:																	#Ellers.
		return 0.75															#Returnér 0.75 (75 %).

print("Indtast din alder: ")												#Udskriver "<TEXT>" til terminalen

alder = input()																#Inputtet fra terminalen gemmes i variablen alder.

print("Indtast billetprisen: ")												#Udskriver "<TEXT>" til terminalen

pris = input()																#Inputtet fra terminalen gemmes i variablen pris.

print("Din pris er: " + str(float(pris) * getPrice(int(alder))) + " Kr.")	#Udskriver "<TEXT>" sammensat med pris * resultatet af getPrice.
