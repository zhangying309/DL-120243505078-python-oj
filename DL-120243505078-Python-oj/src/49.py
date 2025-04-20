def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
mini, maxi = map(int, input().split())
m = []
i = 0
while True:
    f = fib(i)
    if f >= maxi:
        break
    if f > mini:
        m.append(f)
    i += 1
print(" ".join(map(str, m)))
