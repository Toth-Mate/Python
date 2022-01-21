import random
import os
import time

rnd:int = random.randint(0,9)
tippekSzama:int = 5
tipp:int = None
data:str = ""
siker:bool = False

while(tipp != rnd):
    if(tippekSzama < 1):
        break

    data = input("Találja ki a számot (0 és 9 között): ")

    if(data.isdigit()):
        tipp = int(data)

        if(tipp == rnd):
            siker = True
            break
        else:
            print("Nem találta el a számot!")
    else:
        print("Nem számot adott meg!")
    
    tippekSzama -= 1
    print(f"{tippekSzama} próbákozása maradt!")

    time.sleep(2)
    os.system("cls")



if(siker):
    print("Eltalálta!")
else:
    print(f"Nem sikerült eltalálnia! A szám a {rnd} volt.")