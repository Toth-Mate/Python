import os
import time
import datetime

felhasznaloNev:str = None
szuletesiEv:int = None
kor:int = None

# név bekérése
def nevBeolvasasa() -> str:
    nev:str = None
    while(nev == None):
        data:str = input("Kérem a nevét: ")
        if(len(data) > 3):
            nev =  data
        else:
            print("Túl rövid nevet adott meg!")
            time.sleep(3)
            os.system("cls")

    return nev

# születési év bekérése

def szuletesiEvBekerese() -> int:
    eredmeny:int = None
    ma:datetime = datetime.datetime.now()
    jelenlegiEv:int = int(ma.strftime("%Y"))

    while(eredmeny == None):
        data:str = input("Kérem, adja meg a születési évét! ")

        if(data.isdigit()):
            eredmeny = int(data)
            
            if(eredmeny >= jelenlegiEv):
                eredmeny = None
                print("A születési év nem lehet nagyobb, mint a jelenlegi év!")
                time.sleep(3)
                os.system("cls")
            else:
                return eredmeny
        else:
            print("Nem megfelelő születési évet adott meg!")
            time.sleep(3)
            os.system("cls")

# életkor kiszámítása

def eletkorKiszamitasa(ev:int) -> int:
    jelenlegiEv:int = int(datetime.datetime.now().strftime("%Y"))

    return jelenlegiEv - ev

# kiíratás

def kiiratas(nev:str, ev:int) -> None:
    print(f"{nev}, ön az idén {ev} éves.")


# Főprogram

felhasznaloNev = nevBeolvasasa()
szuletesiEv = szuletesiEvBekerese()

kor = eletkorKiszamitasa(szuletesiEv)

kiiratas(felhasznaloNev, kor)

      #
     ###
    #####
   #######
  #########
   #######
    #####
     ###
      #

