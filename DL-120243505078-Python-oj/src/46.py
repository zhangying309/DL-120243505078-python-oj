import math
a= list(map(int, input().split()))
maxi = -1  
def f(num):
    if num <= 1:
        return False  
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True  
for num in a:
    if num == 0:
        break
    if f(num):
        maxi = max(maxi, num)
if maxi == -1:
    print("no")
else:
    print(maxi)
