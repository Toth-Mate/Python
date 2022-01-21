sum:int = 0
szorzat:int = 1

kezdoErtek:int = int(input("Kezdőérték: "))
vegErtek:int = int(input("Végérték: "))

for i in range(kezdoErtek, vegErtek + 1, 1):
    sum += i
    szorzat *= i

print(f"A megadott intervallum számainak összege: {sum}")
print(f"A megadott intervallum számainak szorzata: {szorzat}")