N = int(input())

if N % 2 == 1:
    print(0)
else:
    k = 0
    N //= 2
    for i in range(1, 100):
        k += N // (5 ** i)
    print(k)