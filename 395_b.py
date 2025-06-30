N = int(input())

ans = [["" for _ in range(N)] for _ in range(N)]

cent = (N-1) / 2

for i in range(N):
    j = N-i
    if i <= j:
        if i % 2 == 0:
            for s in range(i, j):
                for t in range(i, j):
                    ans[s][t] = "#"
        else:
            for s in range(i, j):
                for t in range(i, j):
                    ans[s][t] = "."

for i in range(N):
    print("".join(ans[i]))