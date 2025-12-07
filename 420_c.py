N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in range(N):
    count += min(A[i], B[i])

for _ in range(Q):
    Query = list(map(str, input().split()))
    c = str(Query[0])
    X = int(Query[1]) - 1
    V = int(Query[2])

    if c == "A":
        now = min(A[X], B[X])
        next = min(V, B[X])
        count -= now
        count += next
        print(count)
        A[X] = V
    else:
        now = min(A[X], B[X])
        next = min(A[X], V)
        count -= now
        count += next
        print(count)
        B[X] = V