import os
import time
import random


parosSzam:int = None
paratlanSzam:int = None
rnd:int = None
atlag:float = None
neggyelOszthato:int = 0
tmp:str = ""

while(parosSzam == None):
    tmp = input("Adjon meg egy páros számot! ")

    if(tmp.replace("-","").isdigit()):
        if(int(tmp) % 2 == 0):
            parosSzam = int(tmp)
        else:
            print("Nem páros számot adott meg!")
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")

while(paratlanSzam == None):
    tmp = input("Adjon meg egy páratlan számot! ")

    if(tmp.replace("-","").isdigit()):
        if(int(tmp) % 2 != 0):
            if(int(tmp) > parosSzam):
                paratlanSzam = int(tmp)
            else:
                print("Ennek a számnak nagyobbnak kell lennie az előbb megadott páros számnál!")
        else:
            print("Nem páratlan számot adott meg!")
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")

rnd = random.randint(parosSzam, paratlanSzam)

if(abs(paratlanSzam - rnd) > abs(parosSzam - rnd)):
    print(f"A(z) {paratlanSzam} van messzebb a(z) {rnd}-tól/től.")
elif(abs(paratlanSzam - rnd) < abs(parosSzam - rnd)):
    print(f"A(z) {parosSzam} van messzebb a(z) {rnd}-tól/től.")
else:
    print(f"A(z) {paratlanSzam} és a(z) {parosSzam} ugyanakkora távolságra van a(z) {rnd}-tól/től.")


atlag = (parosSzam + paratlanSzam) / 2
print(f"A két szám átlaga: {atlag}")

for i in range(parosSzam,paratlanSzam+1):
    if(i % 4 == 0):
        neggyelOszthato += 1

print(f"A 4-gyel osztható számok száma {neggyelOszthato}.")
