X, Y, Z = map(int, input().split())

if (X - Z*Y) % (Z-1) == 0 and (X-Z*Y) >= 0:
    print("Yes")
else:
    print("No")