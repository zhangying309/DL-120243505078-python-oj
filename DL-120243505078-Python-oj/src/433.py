n=int(input())
s=[]
r=0
for i in range(2,n+1):
    m=True
    for j in range(2,i):
        if i%j ==0:
            m=False
            break
    if m:
        s.append(i)
print(" ".join(map(str,s)))
print(len(s))
