import math

def f(a, b, c):
    de= b**2 - 4*a*c
    
    if de > 0:
        x1 = (-b - math.sqrt(de)) / (2 * a)
        x2 = (-b + math.sqrt(de)) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        if x1 == int(x1):
            x1 = int(x1)
        else:
            x1 = round(x1, 1)

        if x2 == int(x2):
            x2 = int(x2)
        else:
            x2 = round(x2, 1)
        
        print(f"{x1} {x2}")
    elif de == 0:
        x = -b / (2 * a)
        if x == int(x):
            print(f"{int(x)}")
        else:
            print(f"{root:.1f}")
    else:
        print("none")

a, b, c = map(int, input().split())

f(a, b, c)
