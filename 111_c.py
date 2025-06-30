N = int(input())
V = list(map(int,input().split()))

M = N // 2
A = [V[2*i] for i in range(M)]
B = [V[2*i + 1] for i in range(M)]

Count_A = [[0, i] for i in range(10**5 + 1)]
Count_B = [[0, i] for i in range(10**5 + 1)]
for i in range(M):
    v = A[i]
    Count_A[v][0] += 1
    w = B[i]
    Count_B[w][0] += 1

Count_A.sort(reverse=True)
Count_B.sort(reverse=True)

if Count_A[0][1] != Count_B[0][1]:
    ans = N - Count_A[0][0] - Count_B[0][0]
else:
    ans1 = N - Count_A[1][0] - Count_B[0][0]
    ans2 = N - Count_A[0][0] - Count_B[1][0]
    ans = min(ans1, ans2)
print(ans)