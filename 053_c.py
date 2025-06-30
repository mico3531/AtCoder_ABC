x = int(input())
ans = 0

point = (x//11)*11
ans = (x//11)*2

if point < x:
    point += 6
    ans += 1
if point < x:
    point += 5
    ans += 1

print(ans)