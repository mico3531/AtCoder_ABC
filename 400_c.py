import math

N = int(input())

k = 2
count = 0
while k <= N:
    left = 1
    right = 10 ** 10
    while abs(left-right) > 1:
        middle = (left + right) // 2
        if k * (2*middle - 1)**2 <= N:
            left = middle
        else:
            right = middle - 1
    d = max(1, middle-2)
    while ((2*d-1)**2) * k <= N:
        d += 1
    # print(d-1)
    count += d-1
    k *= 2

print(count)