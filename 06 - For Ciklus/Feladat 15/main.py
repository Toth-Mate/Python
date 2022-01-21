harommalOszthatoSzamokSzama:int = 0

kezdoErtek:int = int(input("Kezdőérték: "))
vegErtek:int = int(input("Végérték: "))

for i in range(kezdoErtek, vegErtek + 1):
    if(i % 2 != 0 and i % 3 == 0):
        harommalOszthatoSzamokSzama += 1

print(f"{harommalOszthatoSzamokSzama} szám osztható hárommal.")
