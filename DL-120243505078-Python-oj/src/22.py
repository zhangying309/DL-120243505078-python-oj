a=int(input())
if a <= 1:
    print(0)
else:
    for i in range(2,a-1):
        if a%i==0:
            x=0
            break
        else:
            x=1
    print(x)
    
