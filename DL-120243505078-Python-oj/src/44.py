import math
n = int(input())
m = []  
for i in range(2, n + 1):
    s = 1
    for j in range(2,int(math.sqrt(i))+1):  
        if i % j == 0:
            s+=j
            if i//j != j:
                s += i//j
    if s == i:
        m.append(i)
print(" ".join(map(str, m)))
