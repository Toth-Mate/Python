#pip3 install keyboard

# csomagok importálása
import os
#import keyboard
import time


# változók definiálása
#   a szám, amit be kell olvasni
#   kezdőértéke None, mivel a while-ciklusban ki tudom ezt használni az ismétlések vizsgálatára
#   vagyis a ciklust mindaddig futtatjuk, amíg a number változónak nem lesz szám értéke
number:float = None

data:str = "" # segédváltozó, a beolvasott értéket fogja tárolni

# while ciklus, ami mindaddig fog futni, amíg a number változó nem kap szám értéket,
# azaz az értéke nem None lesz
while(number == None):
    # beolvasás a konzolról és a beolvasott értéket eltároljuk
    data = input("Kerem a szamot: ")

    # megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható-e
    # mindegy, hogy ez a szám int vagy float típusú
    # idigit() -> bool változó ad vissza
    if(data.isdigit()):
        # ha az isdigit() függvény értéke igaz, akkor számot írt be a felhasználó,
        # amit mi biztos át tudunk szám típussá alakítani
        number = float(data)
    
    # az isdigit() függvény értéke hamis, azaz a felhasználó nem számot írt be
    # így a number változó értéke továbbra is None marad, azaz a felhasználó nem számot írt be
    # a ciklust ismételni kell
    else:
        print("\nNem szamot adott meg!")

        # a programot futtató szálat (thread) elaltatjuk 3 másodpercre
        time.sleep(3)

        # letöröljük a képernyőt
        os.system("cls")



        # egy végtelen while ciklust írunk, mivel arra fogunk várni, hogy a felhasználó
        # lenyomja a kért billentyűt (ENTER)
        """
        print("\nA folytatashoz nyomja meg az ENTER billentyut!")
        while(True):
            # figyeljük, hogy a felhasználó lenyomta-e az ENTER gombot
            if(keyboard.is_pressed('enter')):
                # letöröljük a képernyőt
                os.system("cls")

                # kilépünk a belső (végtelen) while ciklusból
                break
        """

# kiírjuk a beolvasott számot
print(f"A beolvasott szam {number}")
