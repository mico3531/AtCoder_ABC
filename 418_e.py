import math

N = int(input())
X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]

for i in range(N):
    X[i], Y[i] = list(map(int, input().split()))

D_1 = dict()
D_2 = dict()

for i in range(N-1):
    for j in range(i+1, N):
        a = X[i] - X[j]
        b = Y[i] - Y[j]
        if a < 0:
            a *= -1
            b *= -1
        if a == 0 and b < 0:
            b *= -1
        
        if (a, b) in D_2:
            D_2[(a, b)] += 1
        else:
            D_2[(a, b)] = 1

        if a != 0 and b != 0:
            g = math.gcd(abs(a), abs(b))
            a //= g
            b //= g
            if (a, b) in D_1:
                D_1[(a, b)] += 1
            else:
                D_1[(a, b)] = 1
        elif a == 0:
            if (0, 1) in D_1:
                D_1[(0, 1)] += 1
            else:
                D_1[(0, 1)] = 1
        else:
            if (1, 0) in D_1:
                D_1[(1, 0)] += 1
            else:
                D_1[(1, 0)] = 1

# print(D_1)
# print(D_2)

ans = 0

for x in D_1:
    ans += D_1[x] * (D_1[x] - 1) * 2

# print(ans)

for x in D_2:
    ans -= D_2[x] * (D_2[x] - 1)

print(ans // 4)