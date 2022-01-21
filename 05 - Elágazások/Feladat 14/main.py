
print("x = ")
x:int = int(input())

print("y = ")
y:int = int(input())

print("z = ")
z:int = int(input())

if(x % y == 0 and x % z == 0):
    print(f"{x} osztható {y} és {z} számokkal.")
elif(x % y == 0):
    print(f"{x} osztható a(z) {y} számmal.")
elif(x % z == 0):
    print(f"{x} osztható a(z) {z} számmal.")
else:
    print(f"{x} nem osztható se a(z) {y}, se a(z) {z} számmal.")
