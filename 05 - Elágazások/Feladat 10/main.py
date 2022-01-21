
print("x = ")
x:int = int(input())

if(x % 2 == 0 and x % 3 != 0):
    print("BIZ")
elif(x % 3 == 0 and x % 2 != 0):
    print("BAZ")
elif(x % 3 == 0 and x % 2 == 0):
    print("ZIZI")
else:
    print(f"{x} se 2-vel, se 3-mal nem osztható.")
