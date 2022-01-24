import os
import time

# 
pontszam:int = None
erdemjegy:int = None

def hiba(uzenet:str) -> None:
    print(uzenet)

    time.sleep(2)
    os.system("cls")

# pontszám bekérése
def  pontBekeres() -> int:
    pontszam:int = None

    while(pontszam == None):
        tmp:str = input("Adja meg a dolgozat pontszámát! ")

        if(tmp.isdigit()):
            pontszam = int(tmp)

            if(pontszam >= 0 and pontszam <= 100):
                return pontszam
            else:
                pontszam = None
                hiba("0 és 100 között adhat csak meg értéket!")
        else:
            hiba("Nem számot adott meg!")




# pontszám vizsgálata
def vizsgalat(_pontszam:int) -> int:
    if(_pontszam < 50):
        return 1
    elif(_pontszam >= 50 and _pontszam < 60):
        return 2
    elif(_pontszam >= 60 and _pontszam < 70):
        return 3
    elif(_pontszam >= 70 and _pontszam < 85):
        return 4
    else:
        return 5

# kiírás
def kiiratas(_pszam:int, _osztalyzat:int) -> None:
    print(f"Ön {_pszam} pontszámot ért el, így az érdemjegye {_osztalyzat}.")

# Főprogram

pontszam = pontBekeres()
erdemjegy = vizsgalat(pontszam)

kiiratas(pontszam, erdemjegy)
