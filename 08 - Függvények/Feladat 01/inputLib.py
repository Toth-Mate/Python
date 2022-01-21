import os
import time

def tizedesSzamBeolvasasa(szoveg:str) -> float:
    szam:float = None
    tmp:str = ""

    while(szam == None):
        tmp = input(szoveg)

        if(tmp.replace("-", "").replace(".", "").isdigit()):
            szam = float(tmp)
        else:
            print("Nem számot adott meg!")
        
        time.sleep(2)
        os.system("cls")
    
    return szam

def egeszSzamBeolvasasa(szoveg:str) -> int:
    szam:int = None
    tmp:str = ""

    while(szam == None):
        tmp = input(szoveg)

        if(tmp.replace("-", "").replace(".", "").isdigit()):
            szam = int(tmp)
        else:
            print("Nem számot adott meg!")
        
        time.sleep(2)
        os.system("cls")
    
    return szam