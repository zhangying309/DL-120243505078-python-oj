
hours = int(input())
if hours <= 10:
    fee = 30
elif hours <= 50:
    fee = hours * 3
else:
    fee = hours * 2.5
print(int(fee))  
