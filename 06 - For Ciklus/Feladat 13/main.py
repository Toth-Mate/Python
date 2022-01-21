parosSzamokOsszege:int = 0
paratlanSzamokOsszege:int = 0

kezdoErtek:int = int(input("Kezdőérték: "))
vegErtek:int = int(input("Végérték: "))

for i in range(kezdoErtek, vegErtek + 1):
    if(i % 2 == 0):
        parosSzamokOsszege += i
    else:
        paratlanSzamokOsszege += i

if(parosSzamokOsszege > paratlanSzamokOsszege):
    print("A páros számok összege a nagyobb.")
elif(paratlanSzamokOsszege > parosSzamokOsszege):
    print("A páratlan számok összege a nagyobb.")
else:
    print("Ugyanannyi a páros- és a páratlan számok összege!")

