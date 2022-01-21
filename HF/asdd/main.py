
kezdoErtek:int = int(input("Adja meg a kezdőértéket: "))
vegErtek:int = int(input("Adja meg a végértéket: "))

if(vegErtek % 2 != 0):
	vegErtek -= 1

for i in range(vegErtek, kezdoErtek, -2):
	print(i)

