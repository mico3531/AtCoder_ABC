def solve(N: int, P: list[int]):
    next_P = []
    sect_size = 2
    sect_count = 2 ** (N-1)
    pre_size = 1
    for i in range(N):
        for j in range(sect_count):
            p = j*sect_size
            q = j*sect_size + pre_size
            r = j*sect_size + sect_size
            A = P[p: q]
            B = P[q: r]
            if A < B:
                next_P += A + B
            else:
                next_P += B + A
        P = next_P
        next_P = []
        sect_size *= 2
        sect_count //= 2
        pre_size *= 2
    print(*P)

T = int(input())

for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    solve(N, P)