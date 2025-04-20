nums = list(map(int,input().split()))
s=0
for num in nums:
    num = int(num)
    if num == 0:
        break
    if num%2 !=0:
        s+=num
print(s)
