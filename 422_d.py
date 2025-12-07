N, K = map(int, input().split())

base = K // (2 ** N)
r = K % (2 ** N)

Ls = [0 for _ in range(2 ** (N+1))]
Ls[1] = r
for i in range(1, 2 ** N):
    x = Ls[i]
    p = x // 2
    q = x - p
    Ls[2*i] = p
    Ls[2*i + 1] = q

Ans = [base + Ls[i + 2 ** N] for i in range(2**N)]

if r == 0:
    print(0)
else:
    print(1)
print(*Ans)