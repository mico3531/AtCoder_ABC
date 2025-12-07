X, Y = map(int, input().split())

Z = (X + Y) % 12
if Z == 0:
    Z = 12

print(Z)