a,*b = map(int,input().split())
p,l=0,0
for i in b:
    if i%2 == 0:
        l+=i**3
    elif i%2 !=0:
        p+=i**2
print(p,l)
