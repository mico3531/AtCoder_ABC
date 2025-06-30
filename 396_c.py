N, M = map(int,input().split())
B = list(map(int,input().split()))
W = list(map(int,input().split()))
B.sort(reverse = True)
W.sort(reverse = True)

sumB = [0 for _ in range(N+1)]
for i in range(N):
    sumB[i+1] = sumB[i] + B[i]

sumW = [0 for _ in range(M+1)]
for j in range(M):
    sumW[j+1] = sumW[j] + W[j]

# print(sumB)
# print(sumW)

ans = 0
j = 0
for i in range(N+1):
    while j < M and j < i:
        if sumW[j+1] > sumW[j]:
            j += 1
        else:
            break
    ans = max(sumB[i] + sumW[j], ans)

print(ans)