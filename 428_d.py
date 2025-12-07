import math

def solve():
    C, D = map(int, input().split())
    a = math.floor(math.log10(C+1))
    b = math.ceil(math.log10(C+D))

    ans = 0
    for i in range(a, b):
        p = max(10**i, C+1)
        q = min(10**(i+1) -1, C+D)
        s = max(0, math.ceil(math.sqrt(10**(i+1) * C + p)) - 10)
        while s**2 < 10**(i+1) * C + p:
            s += 1
        t = math.floor(math.sqrt(10**(i+1) * C + q)) + 10
        while 10**(i+1) * C + q < t**2:
            t -= 1
        if s <= t:
            ans += t-s+1
    
    print(ans)

T = int(input())

for _ in range(T):
    solve()