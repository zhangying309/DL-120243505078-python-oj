b=list(map(int,input().split()))
n=0
x=b[0]
for num in b:
    if num==0:
        break
    n += 1
    if num>x:
        x=num
print(n,x)
