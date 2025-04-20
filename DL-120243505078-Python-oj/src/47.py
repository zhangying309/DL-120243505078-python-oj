import math
def f(num):
    count = 0
    for i in range(1,num+1):
        if num % i ==0:
            count += 1
    return count
data = list(map(int ,input().split()))
n=data[0]
nums = data[1:]
s=0
for num in nums:
    s+=f(num)
print(s)
            
