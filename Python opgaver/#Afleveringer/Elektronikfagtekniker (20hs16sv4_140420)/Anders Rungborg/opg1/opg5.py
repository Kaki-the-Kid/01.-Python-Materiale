# Anders Chr. Rungborg
# 15-04-2020
# OPG Python

age = input("hvor gammel er du? ")         # har har vi en varbel som der er styer af fors input 

def rating(age):                           # 
    if int (age)<13:                       # har age er ubder 13 skal den return med PG
        return "PG"                        # skiver tilbage 
    
    elif int(age)<18 and int(age)>12:      # her tjegger den om den er onder 18 men over 12 
        return "din rating er PG-13"
    
    else:
    
        return "Din rating er R"            # elesers kommer den Din rating er R 

print(rating(age))
