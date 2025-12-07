N, Q = map(int, input().split())
A = list(map(int, input().split()))

new_A = A + A
sum_A = [0 for _ in range(1 + 2*N)]
for i in range(1, 1+2*N):
    sum_A[i] = sum_A[i-1] + new_A[i-1]

# print(new_A)
# print(sum_A)

count = 0

for _ in range(Q):
    Query = list(map(int, input().split()))
    if Query[0] == 1:
        c = Query[1]
        count += c 
        count %= N
    else:
        l = Query[1] + count
        r = Query[2] + count
        ans = sum_A[r] - sum_A[l-1]
        print(ans)