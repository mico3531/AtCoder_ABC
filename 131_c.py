import math

A, B, C, D = map(int,input().split())

E = math.lcm(C, D)

ans = B-A+1
ans -= ((B // C) - ((A-1) // C))
ans -= ((B // D) - ((A-1) // D))
ans += ((B // E) - ((A-1) // E))

print(ans)