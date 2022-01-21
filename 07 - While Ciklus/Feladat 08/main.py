import os
import time
from typing import *

data:str = ""
uditoSzama:int = None
uditok:str = "Limonádé;Coca Cola;Fanta;Narancslé;Kinley"
udito:str = ""

while(uditoSzama == None):
    print("1.) Limonádé\n2.) Coca Cola\n3.) Fanta\n4.) Narancslé\n5.) Kinley")

    data = input("Adja meg, milyen üdítőt szeretne az üdítő számával! ")

    if(data.replace("-", "").isdigit()):
        if(int(data) < 1 or int(data) > 5):
            print("Ilyen üdítő nincs az automata kínálatában!")
        else:
            uditoSzama = int(data)
    else:
        print("Nem számot adott meg!")

    time.sleep(2)
    os.system("cls")

udito = uditok.split(";")[uditoSzama - 1]

print(f"Tessék, itt a(z) {udito}-ja/je!")
