from pickletools import int4
import random
import os
import time


szam1:int = None
szam2:int = None
kitalalandoSzam:int = None

def hibaUzenet(szoveg:str, kesleltetesMerteke:int) -> None:
    print(szoveg)

    time.sleep(kesleltetesMerteke)
    os.system("cls")


def szamBeolvasasa(kezdoErtek:int, vegErtek:int) -> int:
    eredmeny:int = None

    while(eredmeny == None):
        data:str = input(f"Adjon meg egy számot {kezdoErtek} és {vegErtek} között! ")

        if(data.isdigit()):
            if(int(data) >= kezdoErtek and int(data) <= vegErtek):
                eredmeny = int(data)
            else:
                hibaUzenet(f"A számnak {kezdoErtek} és {vegErtek} közé kell esnie!", 3)
        else:
            hibaUzenet("Nem számot adott meg!", 3)
    
    return eredmeny

def randomSzamGeneralas(kezd:int, veg:int) -> int:
    return random.randint(kezd, veg)

def sikeresTipp(probakSzama:int, szam:int) -> None:
    print("Gratulálok! Kitalálta a számot!")
    print(f"{probakSzama} probálkozása volt\nA szám a {szam} volt.")

def sikertelenTipp(tipp:int, szam:int) -> None:
    if(tipp > szam):
        hibaUzenet("Nagyobbat tippelt a számnál!", 2)
    else:
        hibaUzenet("Kisebbet tippelt a számnál!", 2)

def tippBeolvasas() -> int:
    eredmeny:int = None

    while(eredmeny == None):
        data:str = input("Tippelje meg a számot! ")

        if(data.isdigit()):
            eredmeny = int(data)
        else:
            hibaUzenet("Nem számot adott meg!", 2)
    
    return eredmeny

def jatek(szam:int) -> None:
    probakSzama:int = 0
    ertek:int = None

    while(ertek != szam):
        probakSzama += 1

        ertek = tippBeolvasas()

        if(ertek == szam):
            sikeresTipp(probakSzama, ertek)
        else:
            sikertelenTipp(ertek, szam)

szam1 = szamBeolvasasa(0,9)
szam2 = szamBeolvasasa(40,50)
kitalalandoSzam = randomSzamGeneralas(szam1, szam2)

jatek(kitalalandoSzam)
