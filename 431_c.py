N, M, K = map(int, input().split())
H = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

H = H[:K]
H.reverse()
B = B[:K]
# print(H)
# print(B)

ans = "Yes"

for i in range(K):
    if H[i] > B[i]:
        ans = "No"

print(ans)