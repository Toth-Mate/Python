import os
import time

n:int = None
m:int = 0
ottelOszthatoSzamokOsszege:int = 0
tizenegyelOszthatoSzamokSzama:int = 0
maradekosOsztas:int = 0
tmp:str = ""

while(n == None):
    tmp = input("Adjon meg egy maximum kétjegyű, pozitív számot! ")

    if(tmp.replace("-","").isdigit()):
        if(int(tmp) >= 0 and int(tmp) <= 99):
            n = int(tmp)
        else:
            print("A megadott szám nem felel meg a feltételeknek!")
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")

# 0-tól n-nig
if(n % 2 != 0):
    m = n - 1
else:
    m = n

for i in range(0,m + 1,2):
    print(i)

# 0-tól n-nig: 5-tel osztható számok összeadása
for i in range(0,n):
    if(i % 5 == 0):
        ottelOszthatoSzamokOsszege += i

print(f"{ottelOszthatoSzamokOsszege} a 0-tól {n}-ig lévő 5-tel osztható számok összege.")

# 0-tól n-nig 11-el osztható számok száma
for i in range(n + 1):
    if(i % 11 == 0):
        tizenegyelOszthatoSzamokSzama += 1

print(f"A 0-tól {n}-ig lévő 11-el osztható számok száma {tizenegyelOszthatoSzamokSzama}.")

# n/7 maradéka 3
for i in range(n):
    if(i % 7 == 3):
        maradekosOsztas += 1

print(f"0-tól {n}-ig {maradekosOsztas} olyan szám van, amely 7-tel osztva 3-at ad maradékul.")
