data = list(map(str, input().split()))
repeat = int(data[0])
results = []
for i in range(1, len(data), 2):
    x = float(data[i])
    n = int(data[i + 1])  
    results.append(f"{x ** n:.6f}".rstrip('0').rstrip('.'))
print(" ".join(results))
