
import os
import time


hatarErtek:int = 0
osszeg:int = 0
lepesek:int = 0
tmp:str = ""


while(hatarErtek < 100):
    tmp = input("Adjon meg egy határértéket! ")

    if(tmp.replace("-", "").isdigit()):
        hatarErtek = int(tmp)

        if(hatarErtek < 100):
            print("A határérték nem lehet kisebb 100-nál!")
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")

temp = ""

while(osszeg < hatarErtek):
    tmp = input("Adjon meg egy számot! ")

    if(tmp.replace("-","").isdigit()):
        osszeg += int(tmp)
    else:
        print("Nem számot adott meg!")
    
    print(f"A jelenlegi összeg: {osszeg}")
    lepesek += 1

    time.sleep(2)
    os.system("cls")

print(f"{lepesek} lépésben sikerült elérnie a határértéket!")
