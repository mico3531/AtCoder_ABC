S_1, S_2 = map(str,input().split())

if S_1 == "sick":
    if S_2 == "sick":
        ans = 1
    else:
        ans = 2
else:
    if S_2 == "sick":
        ans = 3
    else:
        ans = 4

print(ans)