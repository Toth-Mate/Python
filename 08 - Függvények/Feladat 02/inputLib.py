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

def nevBekerese() -> str:
    nev:str = None

    while(nev == None):
        data:str = input("Kérem a nevét! ")
        
        if(len(data) < 3):
            print("Túl rövid a név, minimum 3 karakter!")
            time.sleep(2)
            os.system("cls")
        else:
            nev = data
    
    return nev