#Navn Thomas Suder
#Dato 15/04/2020
#Opgave 7
def myfunc11():
 RATE = 0
 print("You're in luck")
 print("Samlet " + str(RATE) + " kr.")
        
def myfunc23():
 FARE = int(input("What's your fare? "))  
 RATE = 0.7
 print("Samlet " + str(RATE*FARE) + " kr.")

def myfunc64():
 FARE = int(input("What's your fare? "))
 RATE = 1
 print("Samlet " + str(RATE*FARE) + " kr.")
 
def myfuncoldschool():
 FARE = int(input("What's your fare? "))
 RATE = 0.75
 print("Samlet " + str(RATE*FARE) + " kr.")
    

AGE = int(input("What's your age? "))


if AGE in range (0,12):
    myfunc11()
if AGE in range (12,24):
    myfunc23()
if AGE in range (24,65):
    myfunc64()
if AGE > 64:
    myfuncoldschool()

    
    
    
             