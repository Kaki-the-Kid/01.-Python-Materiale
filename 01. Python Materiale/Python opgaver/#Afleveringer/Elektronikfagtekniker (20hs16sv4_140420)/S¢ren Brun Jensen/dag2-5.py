#/bin/python3.7												#Specificerer interpreter

def yourRating(alder):										#Definerer funktionen yourRating med input-parameteret alder
	if int(alder) < 13:										#Hvis alder er mindre end 13
		return "PG"											#returnér strengen "PG"

	elif int(alder) < 18 and int(alder) >= 13:				#Ellers hvis alder er mindre en 18 OG større end, eller lig med, 13
		return "PG-13"										#Returnér strengen "PG-13".

	else:													#Ellers.
		return "R"											#Returnér strengen "R".

print("Hvor gammel er du? ")								#Udskriver "<TEXT>" til terminalen.
alder = input()												#Gemmer inputtet fra terminalen i variablen alder.
print("Du kan se: " + yourRating(alder) + " rated film.")	#Udskriver "<TEXT>" sammensat med resultet fra funktionen yourRating.
