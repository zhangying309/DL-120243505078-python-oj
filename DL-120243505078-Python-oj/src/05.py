time=int(input())
if time<=4:
    wage=50
elif 4<time<=8:
    wage=50+(time-4)*20
elif time>8:
    wage=50+4*20+(time-8)*30
print(wage)
    
