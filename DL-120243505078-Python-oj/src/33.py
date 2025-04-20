a,*p = list(map(int,input().split()))
r=[]
for s in p:
    if s <= 1000:
        t=0
    elif s <= 3000:
        t=int(s*0.03)
    elif s <= 5000:
        t=int(s*0.04)
    else:
        t=int(s*0.06)
    r.append(str(t))
print(' '.join(r))
