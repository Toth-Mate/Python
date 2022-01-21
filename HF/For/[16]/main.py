parosSzamok:int = 0
paratlanSzamok:int = 0
atlag:float = 0

kezdoErtek:int = int(input("Kezdőérték: "))
vegErtek:int = int(input("Végérték: "))

for i in range(kezdoErtek, vegErtek + 1):
	if(i % 2 == 0):
		parosSzamok += i
	else:
		paratlanSzamok += i

atlag = (parosSzamok + paratlanSzamok) / 2

print(f"A páratlan és páros számok összegének átlaga = {atlag}")
