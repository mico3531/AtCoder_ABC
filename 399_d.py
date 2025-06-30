def solve():
    N = int(input())
    A = list(map(int,input().split()))
    pair_dict = dict()
    count = 0
    for i in range(2*N-1):
        if A[i] != A[i+1]:
            a = min(A[i], A[i+1])
            b = max(A[i], A[i+1])
            # print("key is", b*N + a)
            if b*N + a not in pair_dict:
                pair_dict[b*N + a] = i
            elif abs(pair_dict[b*N+a] - i) >= 3:
                count += 1
    if N >= 2:
        for i in range(2*N-3):
            if A[i] == A[i+2] and A[i+1] == A[i+3]:
                count += 1
    return count

T = int(input())
for _ in range(T):
    ans = solve()
    print(ans)