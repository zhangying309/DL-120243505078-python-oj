nums = list(map(int,input().split()))
s=0
for num in nums:
    if num>0:
        s+=num
    else:
        break
print(s)
