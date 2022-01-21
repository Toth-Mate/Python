
print("x = ")
x:int = int(input())

if(x >= 0 and x <= 9):
    print(f"{x} egyjegyű szám.")
elif(x >= 10 and x <= 99):
    print(f"{x} kétjegyű szám.")
elif(x >= 100 and x <= 999):
    print(f"{x} háromjegyű szám.")
elif(x > 999):
    print(f"{x} több, mint háromjegyű szám.")
else:
    print(f"{x} negatív szám.")
