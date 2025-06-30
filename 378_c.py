N = int(input())
A = list(map(int,input().split()))

Dict = dict()
B = [-1 for _ in range(N)]

for i in range(N):
    if A[i] in Dict:
        B[i] = Dict[A[i]]
    Dict[A[i]] = i+1

print(*B)