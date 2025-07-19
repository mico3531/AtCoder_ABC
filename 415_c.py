from collections import deque

def solve(N: int, S: str):
    dp = [False for _ in range(2 ** N)]
    dp[0] = True
    next = deque([0])
    while len(next) > 0:
        x = next.popleft()
        for i in range(N):
            if not((x >> i) & 1):
                y = x + 2**i
                if S[y] == "0" and dp[y] == False:
                    dp[y] = True
                    next.append(y)

    return dp[-1]

T = int(input())
for _ in range(T):
    N = int(input())
    S = "0" + str(input())
    if solve(N, S):
        print("Yes")
    else:
        print("No")