m,n = map(int,input().split())
x=m
while x>=1:
    if m%x == 0 and n%x==0:
        k=x
        break
    x -= 1
print(k)
