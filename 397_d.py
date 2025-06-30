import math

N = int(input())
lim_k = int(N ** (1/3)) + 10

ans_1 = 0
ans_2 = 0
for k in range(1, lim_k):
    if N % k == 0:
        a = 3*k
        b = 3*k*k
        c = k*k*k - N
        D = b*b - 4*a*c
        if D > 0:
            y_1 = int((-b + math.sqrt(D))/(2*a))
            for y in range(y_1 -10, y_1 + 10):
                if y > 0 and (y+k) ** 3 - y ** 3 == N:
                    ans_1 = y+k
                    ans_2 = y
            
            y_2 = int((-b + math.sqrt(D))/(2*a))
            for y in range(y_2 -10, y_2 + 10):
                if y > 0 and (y+k) ** 3 - y ** 3 == N:
                    ans_1 = y+k
                    ans_2 = y

if ans_1 == 0:
    print(-1)
else:
    print(ans_1, ans_2)