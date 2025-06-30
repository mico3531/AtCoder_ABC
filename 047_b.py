W, H, N = map(int,input().split())
L = 0
D = 0

for i in range(N):
    x, y, a = map(int,input().split())
    if a == 2:
        W = min(x, W)
    elif a == 1:
        L = max(x, L)
    elif a == 4:
        H = min(y, H)
    else:
        D = max(y, D)

if L < W and D < H:
    # print(W, L, H, D)
    print((W-L)*(H-D))
else:
    print(0)