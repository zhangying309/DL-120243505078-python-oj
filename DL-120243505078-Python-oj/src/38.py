n = int(input())
s=0
while n>0:
    m=n%10
    if m%2==0:
        s+=m
    n=n//10
print(s)
