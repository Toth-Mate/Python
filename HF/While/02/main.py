import os
import time

szamokOsszege:int = 0
bevitelekSzama:int = 1
bemenet:str = ""

while(szamokOsszege <= 100):
    bemenet = input("Adjon meg egy számot! ")

    if(bemenet.isdigit()):
        szamokOsszege += int(bemenet)
    else:
        print("Nem számot adott meg!")
        time.sleep(2)
    
    
    bevitelekSzama += 1
	print(f"[Bevitel {bevitelekSzama}] A számok jelenlegi összege: {szamokOsszege}.")
	
	time.sleep(2)
	os.system("cls")
