
def f(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
p = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
q = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year, month, day = map(int, input().split())

if f(year):
    month_days = q
else:
    month_days = p

days = sum(month_days[:month-1]) + day
print(days)
