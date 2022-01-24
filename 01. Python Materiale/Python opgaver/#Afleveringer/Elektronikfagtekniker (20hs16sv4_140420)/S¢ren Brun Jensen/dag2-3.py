#/bin/python3.7										#Specificerer interpreter 


import re											#Importerer biblioteket re (RegEx)

string = "Larsten er underviser på AARHUS TECH"		#Gemmer dummy tekst som variablen string

x = re.sub("Larsten", "Karsten", string)			#re.sub funktionen (substitute) bytter alle matches på
													#"Larsten" ud med "Karsten" i variablen string. Denne-
													#modificerede string gemmes i x.

print(x)											#Den nye modificerede strin x udskrives til terminalen
