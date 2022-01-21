piramisMerete:int = int(input("Adja meg a piramis méretét: "))

for i in range(piramisMerete * 2):
    print("", end = "")

    if(i == piramisMerete):
        print(i, end = "")

print()

for i in range(piramisMerete * 2):
    print(" ", end = "")
    
    if(i == piramisMerete - 2):
        print(i)
    
    if(i == piramisMerete):
        print(i)
    
    if(i == piramisMerete + 2):
        print(i)