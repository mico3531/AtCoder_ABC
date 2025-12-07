S = str(input())
N = len(S)

ans = 0

for i in range(N):
    for j in range(i+1, N+1):
        T = S[i:j]
        if len(T) >= 3:
            if T[0] == "t" and T[-1] == "t":
                count = 0
                for k in range(len(T)):
                    if T[k] == "t":
                        count += 1
                ans = max(ans, (count - 2) / (len(T) - 2))

print(ans)