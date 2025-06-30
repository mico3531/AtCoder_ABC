import bisect

N = int(input())
L = list(map(int,input().split()))

L.sort()

# a<=b<=c -> c<a+b<=c+1

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        k = bisect.bisect_right(L, L[i]+L[j]-0.5)-1
        if L[k] < L[i]+L[j] and j < k and k < N:
            # print(i, j, k)
            ans += k-j

print(ans)