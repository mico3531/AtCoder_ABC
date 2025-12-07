N = int(input())
A = list(map(int, input().split()))

ans = "Yes"
exist = set()
for i in range(N):
    if A[i] != -1:
        if A[i] in exist:
            ans = "No"
        else:
            exist.add(A[i])

print(ans)
if ans == "Yes":
    ans_ls = [0 for _ in range(N)]
    num = 1
    for i in range(N):
        if A[i] != -1:
            ans_ls[i] = A[i]
        else:
            while num in exist:
                num += 1
            ans_ls[i] = num
            num += 1
    print(*ans_ls)