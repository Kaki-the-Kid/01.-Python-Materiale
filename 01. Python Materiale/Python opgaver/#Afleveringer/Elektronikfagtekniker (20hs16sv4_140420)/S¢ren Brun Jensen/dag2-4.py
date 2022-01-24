#/bin/python3.7															#Specificerer interpreter

def plusMoms(netto):													#Definerer en funktion med navnet plusMons, med input-parameteret netto
	return float(netto) * 1.25											#returnerer inputtet "netto" gange 1.25. variablen netto castes som float
																		#for, at kunne gange med en anden float.

print("Hvad er nettoprisen på varen? : ")								#Udskriver "<TEXT>" til terminalen.

pris = input()															#Gemmer inputtet fra terminalen i variablen pris

print("Prisen inklussiv moms er: " + str(plusMoms(pris)) + " kr.")		#Udskriver "<TEXT>" og resultatet fra plusMoms-funktionen, casted som string.
