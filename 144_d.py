import math

a, b, x = map(int,input().split())

if a * a * b == x:
    print(0)
elif x < a * a * b / 2:
    # print("over")
    t = (a*b*b)/(2*x)
    ans = math.degrees(math.atan(t))
    print(ans)
else:
    # print("shallow")
    diff = a * a * b - x
    t = (2*diff)/(a**3)
    ans = math.degrees(math.atan(t))
    print(ans)