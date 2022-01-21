szamokSzama:int = 0
osszesSzam:int = 0
atlag:float = 0

kezdoErtek:int = int(input("Kezdőérték: "))
vegErtek:int = int(input("Végérték: "))

for i in range(kezdoErtek, vegErtek + 1):
    szamokSzama += 1
    osszesSzam += i

atlag = osszesSzam / szamokSzama

print(f"A számok átlaga: {atlag}")
