# I. név nem lehet üres string!
# II. szóköz (1 vagy több)
# III. név hossza!

import os
import time

nev:str = ""
hiba:bool = True

while(hiba):
    nev = input("Neve: ")

    if(nev == ""):
        print("Nem adott meg nevet!")
        time.sleep(2)
        os.system("cls")
    elif(nev.isspace()):
        print("A név nem tartalmazhat ennyi szóközt!")
        time.sleep(2)
        os.system("cls")
    elif(len(nev) < 3):
        print("A névnek legalább 3 karakter hosszúnak kell lennie!")
        time.sleep(2)
        os.system("cls")

    hiba = nev == "" or nev.isspace() or len(nev) < 3

print(f"Az Ön neve: {nev}")
