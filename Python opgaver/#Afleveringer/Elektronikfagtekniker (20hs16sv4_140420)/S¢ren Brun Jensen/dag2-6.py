#/bin/python3.7							#Specificerer interpreter

def replaceNumbers(n):					#Definerer funktionen replaceNumbers med input-parameteret n.
	if (n % 3) == 0:					#Hvis n % 3 = 0 (n går op i 3).
		if (n % 5) == 0:				#(og) hvis n % 5 = 0 (går op i 5).
			return "vaniljebudding"		#Returnér strengen "vaniljebudding".
		else:							#Ellers.
			return "vanilje"			#n går op i 3 men ikke i 5. returnér strengen "vanilje".
	elif (n % 5) == 0 and (n % 3) > 0:	#Eller hvis n går op i 5 og n ikke går op i 3.
		return "budding"				#Returnér strengen "budding".

	else:								#Ellers.
		return n 						#Returnér n.

for x in range(0,25):					#Kør indholdet af for-loopet 25 gange. x bliver talt op hver gang loopet køres.
	print(replaceNumbers(x))			#Udskriver resultatet af replaceNumber-funktionen. Hvor inputtet er x fra for-loopet.
