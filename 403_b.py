T = str(input())
U = str(input())

ans = "No"
for i in range(len(T) - len(U) + 1):
    sub_T = T[i: i+len(U)]
    check = True
    for j in range(len(U)):
        if sub_T[j] != "?" and sub_T[j] != U[j]:
            check = False
    if check:
        ans = "Yes"

print(ans)