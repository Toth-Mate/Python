eredmeny:int = 0
muvelet:bool = True

kezdoErtek:int = int(input("Kezdőérték: "))
vegErtek:int = int(input("Végérték: "))

for i in range(kezdoErtek, vegErtek + 1):
    if(muvelet):
        eredmeny += i
    else:
        eredmeny -= i
    
    muvelet = not(muvelet)

print(eredmeny)
