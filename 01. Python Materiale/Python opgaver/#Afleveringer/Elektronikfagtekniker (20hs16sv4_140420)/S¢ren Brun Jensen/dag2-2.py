#/bin/python3.7															#Specificerer interpreter

import re																#importerer biblioteket re (RegEx)

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."		#Gemmer dummy tekst i variablen string

x = re.search("ipsum", string)											#Bruger re-funktionen search, fra re-biblioteket, til at finde
																		#et match på "ipsum" i string. funktionen returnerer et re.object,
																		#der indeholder et eventuelt match. Objektet gemmes i x

print(x.group())														#Udskriver match fra re.search funktionen vha. x.group() funktionen.
																		#.group() er en metode der er til rådighed for re.object klasser. 
