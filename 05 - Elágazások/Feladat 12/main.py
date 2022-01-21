
print("x = ")
x:int = int(input())

if(10 <= x <= 20):
    print(f"{x} 10 és 20 közé esik.")
elif(-20 <= x <= -10):
    print(f"{x} -10 és -20 közé esik.")
else:
    print(f"{x} nem esik se -10 és -20, se 10 és 20 közé.")
