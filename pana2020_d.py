N = int(input())
alps = "abcdefghij"

Ans = []

def dfs(S, i):
    if len(S) == N:
        Ans.append(S)
    else:
        for j in range(i):
            dfs(S+alps[j], i)
        dfs(S+alps[i], i+1)

dfs("a", 1)
for S in Ans:
    print(S)
print(len(Ans))