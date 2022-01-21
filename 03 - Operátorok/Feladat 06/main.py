
print("Adja meg az első számot: ")
x:float = float(input())

print("Adja meg a második számot:")
y:float = float(input())

print("Adja meg a harmadik számot: ")
z:float = float(input())

eredmeny:float = ((x + 0.5) * (y - 0.7)) % z
print(f"[({x} + 0.5) * ({y} - 0.7)] % {z} = {eredmeny}")
