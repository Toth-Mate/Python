
kezdoErtek:int = int(input("Kezdőérték: "))
vegErtek:int = int(input("Végérték: "))

if(kezdoErtek % 2 == 0):
    kezdoErtek += 1

for i in range(kezdoErtek, vegErtek, 2):
    print(i)