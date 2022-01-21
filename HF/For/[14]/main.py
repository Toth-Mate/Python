hettelOszthatoSzamokOsszege:int = 0
ottelOszthatoSzamokOsszege:int = 0

kezdoErtek:int = int(input("Kezdőérték: "))
vegErtek:int = int(input("Végérték: "))

for i in range(kezdoErtek, vegErtek + 1):
	if(i % 5 == 0 and i % 7 == 0):
		ottelOszthatoSzamokOsszege += i
		hettelOszthatoSzamokOsszege += i
	elif(i % 5 == 0):
		ottelOszthatoSzamokOsszege += i
	elif(i % 7 == 0):
		hettelOszthatoSzamokOsszege += i

if(ottelOszthatoSzamokOsszege > hettelOszthatoSzamokOsszege):
	print("Az 5-tel osztható számok összege a nagyobb.")
elif(ottelOszthatoSzamokOsszege < hettelOszthatoSzamokOsszege):
	print("A 7-tel osztható számok összege a nagyobb.")
else:
	print("Az 5-tel és a 7-tel osztható számok összege egyenlő.")
