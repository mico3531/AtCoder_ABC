import math

A, B, X = map(int,input().split())

def cost(N):
    d = math.floor(math.log10(N)) + 1
    return A*N + B*d

if A + B > X:
    print(0)
else:
    left = 1
    right = 10 ** 9

    while right - left >= 2:
        middle = (left + right) // 2
        if cost(middle) >= X:
            right = middle
        else:
            left = middle
        # print(left, right)
    
    ans = min(10 ** 9, right+1)
    while cost(ans) > X:
        ans -= 1
    print(ans)