N = int(input())
A = list(map(int,input().split()))

dict_1 = dict()
dict_2 = dict()

for i in range(N):
    if A[i] not in dict_2:
        dict_2[A[i]] = 1
    else:
        dict_2[A[i]] += 1

ans = 0
for i in range(N-1):
    dict_2[A[i]] -= 1
    if dict_2[A[i]] == 0:
        dict_2.pop(A[i])
    
    if A[i] not in dict_1:
        dict_1[A[i]] = 1
    else:
        dict_1[A[i]] += 1
    
    ans = max(ans, len(dict_1) + len(dict_2))

print(ans)