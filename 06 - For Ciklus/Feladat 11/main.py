parosSzamokOsszege:int = 0
paratlanSzamokSzorzata:int = 1

print("Kezdőérték = ")
kezdoErtek:int = int(input())
print("Végérték = ")
vegErtek:int = int(input())

for i in range(kezdoErtek, vegErtek + 1):
    if(i % 2 == 0):
        parosSzamokOsszege += i
    else:
        paratlanSzamokSzorzata *= i

print(f"Páros számok összege: {parosSzamokOsszege}")
print(f"Páratlan számok szorzata: {paratlanSzamokSzorzata}")
