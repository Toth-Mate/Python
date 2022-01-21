import os
import time

penz:float = None
honapokSzama:int = 0
tmp:str = ""

while(penz == None):
    tmp = input("Adja meg, mennyi megtakarított pénze van a bankban! ")

    if(tmp.isdigit()):
        if(float(tmp) >= 10000 and float(tmp) <= 50000):
            penz = float(tmp)
        else:
            print("A pénze 10.000 és 50.000 között lehet csak!")
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")

while(penz < 100000):
    penz *= 1.02
    honapokSzama += 1

print(f"{honapokSzama} hónap alatt éri el a pénze a 100.000-et.")
