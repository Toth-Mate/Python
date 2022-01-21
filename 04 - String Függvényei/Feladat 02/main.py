# split

from typing import *

text:str = "bonjour le monde"
textAsList:List[str] = text.split()

print(textAsList)

##
text = "Katarzyna Skoworonska Dolata;Polland;190;center"
textAsList = text.split(";")
print(textAsList)
