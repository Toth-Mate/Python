from inputLib import tizedesSzamBeolvasasa
from mFuggvenyek import *

szam1:float = None
szam2:float = None
osszeg:float = None
kulonbseg:float = None
szorzat:float = None
hanyados:float = None


szam1 = tizedesSzamBeolvasasa("Kérem az első számot! ")
szam2 = tizedesSzamBeolvasasa("Kérem a második számot! ")

osszeg = osszeadas(szam1, szam2)
kulonbseg = kivonas(szam1, szam2)
szorzat = szorzas(szam1, szam2)
hanyados = osztas(szam1, szam2)

print(f"A két szám összege: {osszeg}")
print(f"A két szám különbsége: {kulonbseg}")
print(f"A két szám szorzata: {szorzat}")
print(f"A két szám hányadosa: {hanyados}")
