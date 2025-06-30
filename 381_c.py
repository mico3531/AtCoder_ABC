N = int(input())
S = str(input())

Ls1 = [-1 for _ in range(N)]
j = N-1
for i in range(N-1, -1, -1):
    if S[i] == "/":
        if j > i:
            j = i
            while j-1 >= 0:
                if S[j-1] == "1":
                    j -= 1
                else:
                    break
        Ls1[i] = i-j

Ls2 = [-1 for _ in range(N)]
j = 0
for i in range(N):
    if S[i] == "/":
        if j < i:
            j = i
            while j+1 < N:
                if S[j+1] == "2":
                    j += 1
                else:
                    break
        Ls2[i] = j-i

ans = 1
for i in range(N):
    if S[i] == "/":
        k = min(Ls1[i], Ls2[i])
        ans = max(ans,1 + 2*k)

print(ans)