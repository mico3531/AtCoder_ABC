N, M = map(int,input().split())
A = set(map(int,input().split()))

Ansls = []
for i in range(1, N+1):
    if i not in A:
        Ansls.append(i)

print(len(Ansls))
print(*Ansls)