import os
import time

szam:int = 0
tmp:str = ""

while(szam < 100 or szam > 999):
    tmp = input("Adjon meg egy háromjegyű számot! ")
    
    if(tmp.replace("-", "").isdigit()):
        szam = int(tmp)

        if(szam < 100 or szam > 999):
            print("A szám nem a megfelelő intervallumban van!")
    else:
        print("Nem számot adott meg!")

    time.sleep(2)
    os.system("cls")


if(szam % 7 == 0):
    print(f"{szam} osztható 7-tel.")
else:
    print(f"{szam} nem osztható 7-tel.")
