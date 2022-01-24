# Anders Chr. Rungborg
# 15-04-2020
# OPG Python

import random                                          # her kommer den med random tal

number = random.randint(1, 20)                         # har bliver det specificeret tal grupen den skal være ind for 
tries = 1                                              # har siger at min for et forsøge  

print("jeg tænger på et nummer imen 1 og 20 ")         #
guess = int(input("have a guess: "))                   # dit svar
if guess > number:                                     # har vis dit svar er højere end det random nummer skiver den "guess loer..."
    print("guess loer...")                             

if guess < number:
    print("guess higher...")
    