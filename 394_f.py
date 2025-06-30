import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# print(G)
DP = [0 for _ in range(N)]
ans = -1
def dfs(x, pre):
    global ans
    temp = []
    for y in G[x]:
        if y != pre:
            dfs(y, x)
            temp.append(DP[y])
    
    temp.sort(reverse=True)
    # DPの更新
    if len(temp) < 3:
        DP[x] = 1
    else:
        DP[x] = sum(temp[:3]) + 1
    
    # ansの更新
    if len(temp) >= 4:
        ans = max(ans, sum(temp[:4]) + 1)
    elif len(temp) >= 1:
        ans = max(ans, temp[0] + 1)
    return DP[x]

dfs(0, -1)
# print(DP)
# print(Ls)
# print(ans)

if ans <= 2:
    print(-1)
else:
    print(ans)