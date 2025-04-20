
weight = float(input())
if weight <= 50:
    fee = weight * 0.15
else:
    fee = weight * 0.15 + (weight - 50) * 0.10
print(f"{fee:.2f}".rstrip('0').rstrip('.'))
