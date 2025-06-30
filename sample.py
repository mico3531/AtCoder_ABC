N, x = map(int,input().split())
A = list(map(int,input().split()))

nums = set([0])
dist = 0
Ansls = ["0" for _ in range(N)]
for i in range(N):
    nums.add(dist-A[i])
    print(x - A[i], nums)
    if x - A[i] in nums:
        Ansls[i] = "1"
    dist -= A[i]
    x -= A[i]

print(Ansls)