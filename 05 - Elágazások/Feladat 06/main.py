
print("x = ")
x:int = int(input())

print("y = ")
y:int = int(input())

print("z = ")
z:int = int(input())

if(x < y < z):
    print(f"{x}; {y}; {z}")


"""
    x y z
    x z y
    y x z
    y z x
    z x y
    z y x
    x = y = z
"""