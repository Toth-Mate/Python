
print("Adja meg a kedvenc filmjének címét!")
filmCime:str = str(input())

print("Adja meg a kedvenc filmjének megjelenési évét!")
megjelenesiEv:int = int(input())

print("Adja meg a kedvenc filmjének rendezőjének nevét!")
rendezoNeve:str = str(input())

print("Adja meg a kedvenc filmjének főszereplőjének nevét!")
foszereploNeve:str = str(input())

print(f"{megjelenesiEv}-ban/-ben {rendezoNeve} rendezésében megjelent a/az {filmCime} című film {foszereploNeve} főszereplésével!")
