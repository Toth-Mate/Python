harommalOszthatoSzamokSzama:int = 0

print("Kezdőérték: ")
kezdoErtek:int = int(input())

print("Végérték: ")
vegErtek:int = int(input())

for i in range(kezdoErtek, vegErtek + 1):
    if(i % 3 == 0):
        harommalOszthatoSzamokSzama += 1

print(f"A 3-mal osztható számok száma: {harommalOszthatoSzamokSzama}")



###################
#   ___     ___   #
#    O       O    #
#        ;        #
#    ---------    #
#                 #
###################

