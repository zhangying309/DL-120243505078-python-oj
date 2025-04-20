year,month=map(int,input().split())
def f(year):
    if(year%400==0) or (year%4==0 and year%100 != 0):
        return True
    return False
if month==2:
    if f(year):
        print(29)
    else:
        print(28)
elif month in [1,3,5,7,8,10,12]:
    print(31)
elif month in [4,6,9,11]:
    print(30)
else:
    print("非法月份")
