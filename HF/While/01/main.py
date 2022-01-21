import os
import time

number:int = None
data:str = ""


while(number == None or number < 0 or number > 9):
    data = input("Kérem a számot!\n")
    
    if(data.replace("-", "").isnumeric()):
        number = int(data)

        if(number < 0 or number > 9):
            print("Nem megfelelő a szám (nem 0 és 9 közti)!")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

print(number)
