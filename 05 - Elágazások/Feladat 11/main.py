
print("x = ")
x:int = int(input())

if(x % 2 == 0):
    print(f"{x} páros")
else:
    print(f"{x} páratlan")

if(x < 0):
    print(f"{x} negatív")
elif(x > 0):
    print(f"{x} pozitív")
else:
    print(f"{x} = 0")

if(x % 5 == 0):
    print(f"{x} 5-tel osztható")
else:
    print(f"{x} 5-tel nem osztható")
