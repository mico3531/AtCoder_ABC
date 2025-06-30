a, b, c = map(int,input().split())

if c-a-b > 0 and 4*a*b < (c-a-b) ** 2:
    ans = "Yes"
else:
    ans = "No"
print(ans)