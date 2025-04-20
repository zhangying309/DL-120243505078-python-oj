# 输入三个整数，分别表示三角形的三条边
a, b, c = map(int, input().split())

# 判断是否能构成三角形
if a + b > c and a + c > b and b + c > a:
    print("Yes")
else:
    print("No")
