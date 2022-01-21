import os
import time

kezdoertek:int = None
vegertek:int = None
lepeskoz:int = None
tmp:str = ""

while(kezdoertek == None):
    tmp = input("Adja meg a kezdőértéket! ")

    if(tmp.replace("-","").isdigit()):
        kezdoertek = int(tmp)
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")


while(vegertek == None):
    tmp = input("Adja meg a végértéket! ")

    if(tmp.replace("-","").isdigit()):
        if(int(tmp) > kezdoertek):
            vegertek = int(tmp)
        else:
            print("A végértéknek nagyobbnak kell lennie a kezdőértéknél!")
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")

while(lepeskoz == None):
    tmp = input("Adja meg a lépésközt! ")

    if(tmp.replace("-", "").isdigit()):
        if(int(tmp) < (vegertek - kezdoertek) and int(tmp) != 0):
            lepeskoz = int(tmp)
        elif(int(tmp) == 0):
            print("A lépésköz nem lehet 0!")
        else:
            print("A lépésköznek kisebbnek kell lennie a végérték és a kezdőérték különbségénél!")
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")

if(lepeskoz > 0):
    lepeskoz *= -1


for i in range(vegertek, kezdoertek, lepeskoz):
    print(i)