N = int(input())
S = str(input())

ans = "Yes"
if N % 2 == 0:
    ans = "No"
else:
    for i in range((N-1)//2):
        if S[i] != "1":
            ans = "No"
    if S[(N-1)//2] != "/":
        ans = "No"
    for i in range(1 + (N-1)//2, N):
        if S[i] != "2":
            ans = "No"

print(ans)