C = []
for i in range(3):
    row = list(map(int,input().split()))
    C.append(row)

ans = "No"

if C[0][0] - C[1][0] == C[0][1] - C[1][1] and C[0][0] - C[1][0] == C[0][2] - C[1][2]:
    if C[0][0] - C[2][0] == C[0][1] - C[2][1] and C[0][0] - C[2][0] == C[0][2] - C[2][2]:
        ans = "Yes"

print(ans)