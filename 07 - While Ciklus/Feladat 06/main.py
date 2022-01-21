import os
import time


eletkor:int = None
temp:str = ""

while(eletkor == None):
    temp = input("Adja meg az életkorát! ")

    if(temp.replace("-","").isdigit()):
        if(int(temp) >= 0 and int(temp) <= 99):
            eletkor = int(temp)
        else:
            print("Az életkort 0 és 99 között adja meg!")
    else:
        print("Nem számot adott meg!")
    
    time.sleep(2)
    os.system("cls")

if(eletkor >= 0 and eletkor <= 6):
    print("Gyerek")
elif(eletkor >= 7 and eletkor <= 18):
    print("Iskolás")
elif(eletkor >= 19 and eletkor <= 65):
    print("Dolgozó")
else:
    print("Nyugdíjas")
