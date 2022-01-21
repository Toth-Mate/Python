
print("x = ")
x:int = int(input())

print("y = ")
y:int = int(input())

print("z = ")
z:int = int(input())

#		80		40		20

if(x > y and x > z):
	if(y > z):
		print(f"{z} < {y} < {x}")
	elif(y < z):
		print(f"{y} < {z} < {x}")
	else:
		print(f"{y} = {z} < {x}")
elif(y > x and y > z):
	if(x > z):
		print(f"{z} < {x} < {y}")
	elif(x < z):
		print(f"{x} < {z} < {y}")
	else:
		print(f"{x} = {z} < {y}")
elif(z > x and z > y):
	if(x > y):
		print(f"{y} < {x} < {z}")
	elif(x < y):
		print(f"{x} < {y} < {z}")
	else:
		print(f"{x} = {y} < {z}")
else:
	if(y == z and y == x and z == x):
		print(f"{x} = {y} = {z}")
	elif(y == z):
		print(f"{x} < {y} = {z}")
	elif(x == z):
		print(f"{y} < {x} = {z}")
	elif(x == y):
		print(f"{z} < {x} = {y}")



"""
-	z y x
-	y z x
-	z x y
-	x z y
-	y x z
-	x y z
-	x y = z
-	y x = z
-	z x = y
-	x = y = z
"""
