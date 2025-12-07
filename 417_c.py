N = int(input())
A = list(map(int, input().split()))

A_1 = [A[i] + i for i in range(N)]
A_2 = [j - A[j] for j in range(N)]

dict_1 = dict()
for i in range(N):
    if A[i]+i not in dict_1:
        dict_1[A[i]+i] = 1
    else:
        dict_1[A[i]+i] += 1

dict_2 = dict()
for j in range(N):
    if j-A[j] not in dict_2:
        dict_2[j-A[j]] = 1
    else:
        dict_2[j-A[j]] += 1

ans = 0
for x in dict_1:
    if x in dict_2:
        ans += dict_1[x] * dict_2[x]

print(ans)