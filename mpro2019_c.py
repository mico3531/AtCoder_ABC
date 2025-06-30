K, A, B = map(int,input().split())

ans = K + 1
ans2 = 0

if K >= A-1:
    t1 = A-1
    t2 = (K-t1) // 2
    ans2 = 1 + (K-t2*2) + (B-A) * t2

print(max(ans, ans2))