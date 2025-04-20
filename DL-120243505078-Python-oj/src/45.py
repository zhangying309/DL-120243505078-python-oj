a = list(map(int,input().split()))
s=0
count=0
for num in a:
    if num==0:
        break
    s += num
    count += 1
print(s/count)
